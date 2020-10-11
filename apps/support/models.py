import datetime
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
# 云盘资源
class ResourceType(models.Model):
    name = models.CharField(max_length=100,verbose_name='资源名')
    owner = models.ForeignKey(User, verbose_name='添加人员', null=True, blank=True, on_delete=models.PROTECT)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
    is_delete = models.BooleanField(default=False,  verbose_name="是否删除")
    #TODO 添加逻辑删除
    class Meta:
        verbose_name = '资源类型'
        verbose_name_plural = verbose_name
        ordering = ('add_time',)

    def __str__(self):
        return self.name

class CloundResource(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="资源名")
    url = models.URLField(max_length=500, verbose_name='网盘 地址', blank=True, null=True, default='')
    description = models.TextField(max_length=3000, verbose_name='文件描述', blank=True, null=True, default='')
    type = models.ForeignKey(ResourceType, verbose_name='所属分类', null=True, blank=True, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, verbose_name='上传者', null=True, blank=True, on_delete=models.PROTECT)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    # matchine
    class Meta:
        verbose_name = '教程资源'
        verbose_name_plural = verbose_name
        ordering = ('add_time',)

    def __str__(self):
        return self.name


class WebSiteType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="网站类型")
    order = models.IntegerField(verbose_name='排序索引', default='1')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
    is_delete = models.BooleanField(default=False,  verbose_name="是否删除")
    owner = models.ForeignKey(User, verbose_name='添加人员', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = '网站类型'
        verbose_name_plural = verbose_name
        ordering = ('order',)

    def __str__(self):
        return self.name


class WebSiteLink(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="网站名")
    url = models.URLField(max_length=500, verbose_name='网站地址', blank=True, null=True, default='')
    description = models.TextField(max_length=2000, verbose_name='网站描述', blank=True, null=True, default='')
    type = models.ForeignKey(WebSiteType, verbose_name='所属分类', null=True, blank=True, on_delete=models.PROTECT)
    public = models.BooleanField(verbose_name='是否公开',default=True)
    owner = models.ForeignKey(User, verbose_name='添加人员', null=True, blank=True, on_delete=models.PROTECT)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '网站'
        verbose_name_plural = verbose_name
        ordering = ('add_time',)

    def __str__(self):
        return self.name

STATUS_CHOICE = (
        (0, '待实现'),
        (1, '已实现'),
        (2, '已拒绝'),
)

class Demand(models.Model):
    description = models.TextField(max_length=2000, verbose_name='需求描述', default='')
    owner = models.ForeignKey(User, verbose_name='添加人员', null=True, blank=True, on_delete=models.PROTECT)
    current_state = models.IntegerField(verbose_name='当前状态', choices=STATUS_CHOICE, default=0)
    last_edit_timestamp = models.DateTimeField('保存日期', default=datetime.datetime.now)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = '需求'
        verbose_name_plural = verbose_name
        ordering = ('add_time',)

    def __str__(self):
        return self.description


from mptt.models import MPTTModel, TreeForeignKey


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name