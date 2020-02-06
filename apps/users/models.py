from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,Group


class Role(models.Model):
    name = models.CharField(max_length=32, verbose_name='职位名称')
#多对多关联group模型
    # groups = models.ManyToManyField(to=Group, verbose_name="权限组")

    class Meta:

        verbose_name = '职位管理'

        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# class UserProfileManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         '''username 是唯一标识，没有会报错'''
#         if not username:
#             raise ValueError('Users must have an username')
#         user = self.model(
#             username=username,
#             email=email,
#         )
#         user.set_password(password)  # 检测密码合理性
#         user.save(using=self._db)  # 保存密码
#         return user
#     def create_superuser(self, username, email, password):
#         user = self.create_user(username=username,
#                                 email=email,
#                                 password=password,
#                                 )
#         user.is_admin = True  # 比创建用户多的一个字段
#         user.save(using=self._db)
#         return user

class UserProfile(AbstractUser):
    """
    用户
    """
    # name = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="男", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    department = models.ManyToManyField('Role', verbose_name='部门')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


