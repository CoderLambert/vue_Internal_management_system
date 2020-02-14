import datetime
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=100, blank=True,null=True, unique=True,verbose_name="项目名")
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
    member = models.ManyToManyField(User,  verbose_name=' 项目成员',null=True,blank=True )
    svn = models.CharField(max_length=500, verbose_name='SVN 地址', blank=True, null=True, default='')
    build = models.CharField(max_length=500,verbose_name='Build 脚本参数', blank=True, null=True, default='')

    # matchine
    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name
        ordering = ('add_time',)

    def __str__(self):
        return self.name


class RomImageFile(models.Model):
    name = models.CharField(max_length=100, blank=True,null=True, default='')
    url = models.FileField(upload_to="uploads/images/rom/%Y/%m/%d/", verbose_name="image", null=True, blank=True)
    user = models.ForeignKey(User,  verbose_name='上传用户',null=True,blank=True,on_delete=models.DO_NOTHING )
    project = models.ForeignKey(Project,  verbose_name='所属项目',null=True,blank=True,on_delete=models.DO_NOTHING )
    description = models.TextField(verbose_name='文件描述',null=True,blank=True,default='')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    #TODO 添加逻辑删除
    class Meta:
        verbose_name = 'RomImage'
        verbose_name_plural = verbose_name
        ordering = ('add_time',)

        def __str__(self):
            return self.name


class MachineInfo(models.Model):
    BMC_ip = models.CharField(max_length=100, verbose_name='BMC IP 地址',blank=True,null=True, default='')
    Host_ip = models.CharField(max_length=100, verbose_name='Host IP 地址',blank=True,null=True, default='')
    web_username = models.CharField(max_length=100, verbose_name='Web 用户名',blank=True,null=True, default='admin')
    web_password = models.CharField(max_length=100, verbose_name='Web 密码',blank=True,null=True, default='admin')
    description = models.TextField(verbose_name='机器信息描述',null=True,blank=True,default='')
    user = models.ForeignKey(User, verbose_name='所有者', null=True, blank=True, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, verbose_name='所属项目', null=True, blank=True, on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    #TODO 添加逻辑删除
    class Meta:
        verbose_name = 'MachineInfo'
        verbose_name_plural = verbose_name
        ordering = ('add_time',)

        def __str__(self):
            return self.name
