import logging

from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import mixins, viewsets, authentication, permissions, status

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from .serializers import  UserRegSerializer, UserDetailSerializer,UserOptionListSerializer,RoleSerializer,DepartmentSerializer
from .models import Role,Department
# Create your views here.

# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")

User = get_user_model()
# 手机号码正则表达式
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"

# mixins.DestroyModelMixin,
class UserViewset(mixins.ListModelMixin,mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegSerializer
        if self.action == "list":
            type = self.request.query_params.get('type')
            if type == "options":
                return UserOptionListSerializer
            else:
                return UserDetailSerializer

        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        re_dict["username"] = user.username
        re_dict["userid"] = user.id

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
    # 加上会引起每次都返回当前用户结果   查询指定ID时
    # def get_object(self):
    #     return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class RoleViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )
    permission_classes = []

class DepartmentViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    permission_classes = []
    # permission_classes = (permissions.IsAuthenticated, )



class UserOptionViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    用户选项列表
    """
    serializer_class = UserOptionListSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )







