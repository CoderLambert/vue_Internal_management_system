from django.views import View
from django.contrib.auth.models import AnonymousUser

from .filters import ArticalFilter, NoteFilter, ArticleTypeFilter
from django.http import HttpResponse,JsonResponse,QueryDict
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, viewsets, status, permissions
from articals.models import Articale, Note, ImageMeta, ArticleType
from articals.serializers import ArticaleSerializer, ArticaleCreateSerializer, ArticaleDetailSerializer,ArticleTypeSerializer, NoteSerializer, NoteCreateSerializer, ArticleTypeCreateSerializer, \
    ImageFileSerializer, ImageFileCreateSerializer

from .permission import IsAdminOrArticalOwner
User = get_user_model()


class ImagesPagination(PageNumberPagination):
    # default_limit = 20
    page_size = 5 # 每页数目
    page_query_param = "pagenum"  # 传入的页码数
    page_size_query_param = 'pagesize'  # 前端发送关键字
    max_page_size = 10000

class ArticleTypeListViewSet(viewsets.ModelViewSet):
    """
    获取w文章分类的信息
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = ArticleType.objects.all()
    serializer_class = ArticleTypeSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ArticleTypeSerializer
        elif self.action == "create" or self.action == "update":
            return ArticleTypeCreateSerializer
        return ArticleTypeSerializer

    def get_permissions(self):
        if self.action == "destroy" or self.action == "update" or self.action == "partial_update":
            return [IsAdminOrArticalOwner()]
        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        return []

    filter_class = ArticleTypeFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)

class NoteListViewSet(viewsets.ModelViewSet):
    """
    获取笔记本的信息
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = Note.objects.all().order_by('add_time')
    serializer_class = NoteSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return NoteSerializer
        elif self.action == "create" or self.action == "update":
            return NoteCreateSerializer
        return NoteSerializer

    def get_permissions(self):
        if self.action == "destroy" or self.action == "update" or self.action == "partial_update":
            return [IsAdminOrArticalOwner()]
        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        return []

    filter_class = NoteFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)

class ArticaleListViewSet(viewsets.ModelViewSet):
    """
    获取项目的信息
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = Articale.objects.all().order_by('-modified_time')
    serializer_class = ArticaleSerializer
    pagination_class = ImagesPagination

    def get_queryset(self):
        # project_id may be None
        if self.request.user.id == None:
            return self.queryset \
                .filter(Q(public=True))
        else:
            return self.queryset \
                .filter(Q(public=True) | Q(user=self.request.user))

    def get_serializer_class(self):
        if self.action == "list":
            return ArticaleSerializer
        elif self.action == "create" or self.action == "update":
            return ArticaleCreateSerializer
        elif self.action == "retrieve":
            return ArticaleDetailSerializer
        return ArticaleSerializer

    def get_permissions(self):
        if self.action == "destroy" or self.action == "update" or self.action == "partial_update":
            return [IsAdminOrArticalOwner()]
        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        return []

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.browse_num = instance.browse_num + 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    filter_class = ArticalFilter

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ('text_content','title')
    ordering_fields = ('public','original','browse_num','add_time',)

from rest_framework.parsers import MultiPartParser, FileUploadParser, JSONParser

class ImageMetaListViewSet(viewsets.ModelViewSet):
    """
    获取项目的信息
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = ImageMeta.objects.all().order_by('-add_time')
    parser_classes = (MultiPartParser, JSONParser, FileUploadParser,)
    pagination_class = ImagesPagination

    serializer_class = ImageFileSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ImageFileSerializer
        elif self.action == "create" or self.action == "update":
            return ImageFileCreateSerializer
        return ImageFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # serializer.data.id = serializer.instance.id
        result = {
            'id': serializer.instance.id,
            'image': serializer.instance.image.url
        }
        headers = self.get_success_headers(serializer.data)
        return Response(result, status=status.HTTP_201_CREATED, headers=headers)