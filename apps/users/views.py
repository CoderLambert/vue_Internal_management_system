import logging

from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import mixins, viewsets, authentication, permissions, status

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from .serializers import  UserRegSerializer, UserDetailSerializer,UserSerializer
# Create your views here.

# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")

User = get_user_model()
# 手机号码正则表达式
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):

        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
            if username is None or password is None:
                return
            try:
                user = User._default_manager.get_by_natural_key(username)
            except User.DoesNotExist:
                # Run the default password hasher once to reduce the timing
                # difference between an existing and a nonexistent user (#20760).
                User().set_password(password)
            else:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None
    # def authenticate(self, request, username=None, password=None, **kwargs):
    #     if username is None:
    #         username = kwargs.get(User.USERNAME_FIELD)
    #     if username is None or password is None:
    #         return
    #     try:
    #         user = User._default_manager.get_by_natural_key(username)
    #     except User.DoesNotExist:
    #         # Run the default password hasher once to reduce the timing
    #         # difference between an existing and a nonexistent user (#20760).
    #         User().set_password(password)
    #     else:
    #         if user.check_password(password) and self.user_can_authenticate(user):
    #             return user

class UserViewset(mixins.ListModelMixin,mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        if self.action == "create":
            return UserRegSerializer

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
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["username"] = user.username
        re_dict["userid"] = user.id

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
    # 加上会引起每次都返回当前用户结果   查询指定ID时
    # def get_object(self):
    #     return self.request.user

    def perform_create(self, serializer):
        return serializer.save()
