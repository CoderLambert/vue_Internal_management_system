import chardet

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives  # 引入模块
from django.contrib.auth import get_user_model
from django.conf import settings
from django.template import Context, loader

from rest_framework import mixins, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FileUploadParser, JSONParser
from rest_framework import filters
from .permission import IsAdminOrProjectMember, IsAdminOrMachineOwner
from rest_framework.response import Response

from rest_framework import permissions
from project.filters import RomImagesFilter
from project.models import Project, RomImageFile, MachineInfo
from project.serializers import ProjectSerializer, ProjectCreateSerializer, ProjectNameSerializer, \
    RomImageFileSerializer, RomImageFileListSerializer, \
    RomImageFilePatchSerializer, RomImageFileCreateSerializer, \
    MachineInfoSerializer, CreateMachineSerializer

User = get_user_model()


class ImagesPagination(PageNumberPagination):
    # default_limit = 20
    page_size = 10  # 每页数目
    page_query_param = "pagenum"  # 传入的页码数
    page_size_query_param = 'pagesize'  # 前端发送关键字
    max_page_size = 10000


class ProjecsListViewSet(viewsets.ModelViewSet):
    """
    获取项目的信息
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
    pagination_class = ImagesPagination

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectSerializer
        elif self.action == "create" or self.action == "update":
            return ProjectCreateSerializer
        return ProjectSerializer

    def get_permissions(self):
        if self.action == "destroy":
            return [permissions.IsAdminUser()]
        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update":
            return [IsAdminOrProjectMember()]
        elif self.action == "partial_update":
            return [IsAdminOrProjectMember()]
        return []

    # filter_class = RomImagesFilter
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'svn', 'member__username',)
    # ordering_fields = ('-add_time',)


class ProjectNameListViewSet(mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    """
    项目名列表页
    """
    queryset = Project.objects.all()
    serializer_class = ProjectNameSerializer


class RomImagesListViewSet(viewsets.ModelViewSet):
    """
    image列表页, 分页， 搜索， 过滤， 排序
    """
    # throttle_classes = (UserRateThrottle, )
    # queryset = RomImageFile.objects.all()
    # pagination_class = ImagesPagination
    serializer_class = RomImageFileSerializer
    parser_classes = (MultiPartParser, JSONParser, FileUploadParser,)

    def get_queryset(self):
        # 只有自己的网站和公开的网站才需要返回
        return RomImageFile.objects.filter(Q(is_delete=False))

    def get_serializer_class(self):
        if self.action == "list":
            return RomImageFileSerializer
        elif self.action == "create":
            return RomImageFileListSerializer
        elif self.action in ["partial_update", "update"]:
            return RomImageFilePatchSerializer
        return RomImageFileSerializer

    def get_encoding(file):
        # 二进制方式读取，获取字节数据，检测类型
        with open(file, 'rb') as f:
            data = f.read()
            return chardet.detect(data)['encoding']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        self.release_note_name = serializer.validated_data['release_note'].name
        self.release_note_data = serializer.validated_data['release_note'].file.read()
        self.release_note_data_type = chardet.detect(self.release_note_data)['encoding']
        self.release_note_text = self.release_note_data.decode(self.release_note_data_type)
        self.image_link = serializer.instance[0]['url']
        self.image_name = serializer.validated_data['roms'].name
        self.release_note_link = serializer.instance[0]['release_note']
        self.project_name = serializer.instance[0]['project']
        self.user_name = request.user.username
        self.target_mails = serializer.initial_data['target_mails'].split(',')
        # TODO  发送邮件
        self.sendReleaseNoteMail()
        return Response(serializer.instance, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def sendReleaseNoteMail(self):
        from_email = settings.DEFAULT_FROM_EMAIL
        # user_emails = User.objects.values('email')
        # target_mails = [user['email'] for user in user_emails]

        Subject = '{project_name}项目:  {user_name} 发布了镜像 {image_name}'.format(project_name=self.project_name,
                                                                             user_name=self.user_name,
                                                                             image_name=self.image_name)
        context = {
            'image_link': self.image_link,
            'image_name': self.image_name,
            'release_note_name': self.release_note_name,
            'release_note_text': self.release_note_text,
            'release_note_link': self.release_note_link
        }
        release_image_template = 'release_image.html'
        t = loader.get_template(release_image_template)
        html_content = t.render(context)
        # send_mail(Subject, None, from_email, target_mails,html_message=t.render(context))
        msg = EmailMultiAlternatives(Subject, html_content, from_email, self.target_mails)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    filter_class = RomImagesFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'description', 'user__username', 'add_time')
    ordering_fields = ('add_time',)

    # def perform_create(self, serializer):
    #     serializer.save( name =  ....)


class MachinesListViewSet(viewsets.ModelViewSet):
    """
    机器列表页, 分页， 搜索， 过滤， 排序
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = MachineInfo.objects.all().order_by('project__name')
    serializer_class = MachineInfoSerializer

    # pagination_class = ImagesPagination

    def get_serializer_class(self):
        if self.action == "list":
            return MachineInfoSerializer
        elif self.action == "create" or \
                self.action == "update" or \
                self.action == "partial_update":
            return CreateMachineSerializer
        return MachineInfoSerializer

    def get_permissions(self):
        if self.action == "destroy":
            return [IsAdminOrMachineOwner()]
        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update":
            return [permissions.IsAuthenticated()]
        elif self.action == "partial_update":
            return [permissions.IsAuthenticated()]
        return []

    # filter_class = RomImagesFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('BMC_ip', 'Host_ip', 'project__name', 'description', 'user__username')
    ordering_fields = ('project__name')
