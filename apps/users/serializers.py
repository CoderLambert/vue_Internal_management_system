# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from .models import Role, Department

User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):
    """
    部门序列化
    """

    class Meta:
        model = Role
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    """
    部门序列化
    """

    class Meta:
        model = Department
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    # department = RoleSerializer()
    department = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    role = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = ("id", "username", "is_superuser",
                  "is_staff", "email",
                  "department", "role")


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
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )
    email = serializers.CharField(label="邮箱", help_text="邮箱", required=True, allow_blank=False,
                                  validators=[UniqueValidator(queryset=User.objects.all(), message="邮箱已经存在")])

    class Meta:
        model = User
        fields = ("username", "email", "password", "department", "role")
        # extra_kwargs = {
        #
        #     # 'email': {'required': True},
        #     'password': {'required': True,},
        #     'department': {'required': True,
        #                    'error_messages': {
        #                         'required': '请选择你的所属部门'
        #                     }
        #                 },
        #     'role': {'required': True}
        # }


class UserOptionListSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """

    class Meta:
        model = User
        fields = ("id", "username",)


class UserIDListSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """

    class Meta:
        model = User
        fields = ("id",)


class UserNameListSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """

    class Meta:
        model = User
        fields = ("username",)


class DepartmentSerializer(serializers.ModelSerializer):
    """
    部门序列化类
    """

    class Meta:
        model = Department
        fields = ("id", "name")


class RoleSerializer(serializers.ModelSerializer):
    """
    部门序列化类
    """

    class Meta:
        model = Department
        fields = ("id", "name")


class UserEmailSerializer(serializers.ModelSerializer):
    """
    用户邮箱信息序列化类
    """
    department = DepartmentSerializer(many=True)
    role = RoleSerializer(many=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", 'is_staff', 'department', 'role')
