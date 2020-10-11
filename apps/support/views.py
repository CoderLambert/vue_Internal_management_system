
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework import filters
from rest_framework import permissions
from support.models import WebSiteLink, WebSiteType, ResourceType, CloundResource, Demand
from support.serializers import WebSiteLinkSerializer, WebSiteLinkCreateSerializer,WebSiteTypeSerializer, WebSiteTypeCreateSerializer,\
    ResourceTypeSerializer, ResourceTypeCreateSerializer, CloundResourceSerializer, CloundResourceCreateSerializer,\
    DemandSerializer, DemandCreateSerializer
from .permission import IsAdminOrOwner
from rest_framework.pagination import PageNumberPagination


class CommonPagination(PageNumberPagination):
    # default_limit = 20
    page_size = 10  #每页数目
    page_query_param = "pagenum"  #传入的页码数
    page_size_query_param = 'pagesize' #前端发送关键字
    max_page_size = 10000

class WebSiteTypeListViewSet( viewsets.ModelViewSet):
    """
    获取项目的信息
    """
    queryset = WebSiteType.objects.all()
    serializer_class = WebSiteTypeSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return WebSiteTypeSerializer
        elif self.action == "create" or self.action == "update":
            return WebSiteTypeCreateSerializer
        return WebSiteTypeSerializer

    def get_permissions(self):
        if self.action == "destroy":
            return [permissions.IsAdminUser()]
        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        return []

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'order')
    ordering_fields = ('-add_time',)


class WebSiteLinkListViewSet( viewsets.ModelViewSet):
    """
    获取项目的信息
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = WebSiteLink.objects.all()
    serializer_class = WebSiteLinkSerializer

    def get_queryset(self):
        # 只有自己的网站和公开的网站才需要返回
        return WebSiteLink.objects.filter(Q(owner=self.request.user) | Q(public=True)).order_by('type__order', 'name')

    def get_serializer_class(self):
        if self.action == "list":
            return WebSiteLinkSerializer
        elif self.action == "create" or self.action == "update":
            return WebSiteLinkCreateSerializer
        return WebSiteLinkSerializer

    def get_permissions(self):
        if self.action == "destroy" or self.action == "update":
            return [IsAdminOrOwner()]

        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        return []

    # filter_class = RomImagesFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'url', 'description', 'type__name')
    ordering_fields = ('type',)


class ResourceTypeListViewSet( viewsets.ModelViewSet):
    """
    获取项目的信息
    """
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ResourceTypeSerializer
        elif self.action == "create" or self.action == "update":
            return ResourceTypeCreateSerializer
        return ResourceTypeSerializer

    def get_permissions(self):
        if self.action == "destroy":
            return [permissions.IsAdminUser()]
        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        return []

    search_fields = ('name', 'owner__username',)
    ordering_fields = ('-add_time',)


class DemandListViewSet(viewsets.ModelViewSet):
    """
    获取需求的信息
    """
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer
    pagination_class = CommonPagination

    def get_serializer_class(self):
        if self.action == "list":
            return DemandSerializer
        elif self.action == "create":
            return DemandCreateSerializer
        return DemandSerializer

    def get_permissions(self):
        if self.action == "list":
            return [permissions.IsAuthenticated()]
        return []
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('description', 'owner__username', 'current_state')
    ordering_fields = ('-add_time',)

class CloundResourceListViewSet(viewsets.ModelViewSet):
    """
    获取项目的信息
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = CloundResource.objects.all()
    serializer_class = CloundResourceSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return CloundResourceSerializer
        elif self.action == "create" or self.action == "update":
            return CloundResourceCreateSerializer
        return CloundResourceSerializer

    def get_permissions(self):
        if self.action == "destroy":
            return [permissions.IsAdminUser()]
        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        return []

    search_fields = ('name', 'url', 'description', 'type', 'owner__username',)
    ordering_fields = ('-add_time',)



