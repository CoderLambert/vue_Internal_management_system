from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,Group


class Role(models.Model):
    name = models.CharField(max_length=32, verbose_name='用户角色',unique=True)


    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=32, verbose_name='部门', unique=True)

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):
    """
    用户
    """
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="男", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    department = models.ManyToManyField('Department', verbose_name='部门')
    role = models.ManyToManyField('Role', verbose_name='角色')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


