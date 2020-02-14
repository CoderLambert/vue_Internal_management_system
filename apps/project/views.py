from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins,viewsets,status
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser,FileUploadParser,JSONParser
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

from rest_framework import permissions
from rest_framework import authentication

from project.filters import RomImagesFilter
from project.models import Project, RomImageFile, MachineInfo
from project.serializers import ProjectSerializer,ProjectCreateSerializer, ProjectNameSerializer, RomImageFileSerializer, \
    RomImageFileListSerializer,RomImageFilePatchSerializer, MachineInfoSerializer,CreateMachineSerializer


class ImagesPagination(PageNumberPagination):
    # default_limit = 20
    page_size = 10  #每页数目
    page_query_param = "pagenum"  #传入的页码数
    page_size_query_param = 'pagesize' #前端发送关键字
    max_page_size = 10000


class ProjecsListViewSet( viewsets.ModelViewSet):
    """
    获取项目的信息
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ImagesPagination

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectSerializer
        elif self.action == "create":
            return ProjectCreateSerializer
        return ProjectSerializer

    def get_permissions(self):
        if self.action == "destroy":
            return [permissions.IsAdminUser()]
        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        return []

    # filter_class = RomImagesFilter
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name','svn',)
    # ordering_fields = ('-add_time',)


class ProjecNameListViewSet( mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """
    项目名列表页
    """
    queryset = Project.objects.all()
    serializer_class = ProjectNameSerializer




class RomImagesListViewSet( viewsets.ModelViewSet):
    """
    image列表页, 分页， 搜索， 过滤， 排序
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = RomImageFile.objects.all()
    pagination_class = ImagesPagination
    serializer_class = RomImageFileSerializer
    parser_classes = (MultiPartParser,JSONParser, FileUploadParser,)

    def get_serializer_class(self):
        if self.action == "list":
            return RomImageFileSerializer
        elif self.action == "create":
            return RomImageFileListSerializer
        elif self.action == "partial_update":
            return RomImageFilePatchSerializer
        return RomImageFileSerializer

    filter_class = RomImagesFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name','description','add_time')
    ordering_fields = ('add_time')


class MachinesListViewSet(viewsets.ModelViewSet):
    """
    机器列表页, 分页， 搜索， 过滤， 排序
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = MachineInfo.objects.all()
    serializer_class = MachineInfoSerializer
    pagination_class = ImagesPagination

    def get_serializer_class(self):
        if self.action == "list":
            return MachineInfoSerializer
        elif self.action == "create":
            return CreateMachineSerializer
        return MachineInfoSerializer

    # filter_class = RomImagesFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ( 'BMC_ip','Host_ip', 'project__name', 'description')
    ordering_fields = ('project__name')
