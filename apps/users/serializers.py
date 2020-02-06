# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from .models import Role
User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):

    """
    部门序列化
    """

    class Meta:
        model = Role
        fields ="__all__"

class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    # department = RoleSerializer()
    department = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')

    class Meta:
        model = User
        fields = ("id", "username", "is_superuser",
                  "is_staff", "gender", "groups", "email",
                  "user_permissions", "department")


class UserSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = "__all__"


class UserRegSerializer(serializers.ModelSerializer):

    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    password = serializers.CharField(
        style={'input_type': 'password'},help_text="密码", label="密码", write_only=True,
    )

    department = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "email", "password","department")
