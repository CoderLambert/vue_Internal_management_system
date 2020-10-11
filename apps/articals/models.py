import datetime
import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_delete
from django.dispatch import receiver

User = get_user_model()

class Note(models.Model):
    name = models.CharField(max_length=100, verbose_name="笔记本名称", unique=True)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    user = models.ForeignKey(User, verbose_name='创建者', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = '笔记本'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ArticleType(models.Model):
    name = models.CharField(max_length=100, verbose_name="分类名")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT, verbose_name='父分类')
    user = models.ForeignKey(User, verbose_name='创建者', null=True, blank=True, on_delete=models.PROTECT)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        unique_together = (("name", "parent"),)
        verbose_name = '文章分类标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Articale(models.Model):
    note = models.ForeignKey(Note, verbose_name='笔记本', null=True, blank=True, on_delete=models.PROTECT,
                             related_name="articles")
    title = models.CharField(max_length=100, verbose_name="标题")
    text_content = models.TextField(verbose_name="文章内容文本")
    original = models.BooleanField(default=True, verbose_name="是否原创")
    orginal_link = models.CharField(max_length=300, verbose_name="转载地址", blank=True, null=True)
    public = models.BooleanField(default=True)
    types = models.ManyToManyField(ArticleType, blank=True, null=True, verbose_name='文章分类', related_name="articles")
    browse_num = models.IntegerField(default=0, verbose_name='浏览次数')
    user = models.ForeignKey(User, verbose_name='作者', null=True, blank=True, on_delete=models.PROTECT)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        # ordering = ('types',)

    def __str__(self):
        return self.title


def artical_image_path(instance, filename):
    uid = str(uuid.uuid4())
    subuid = ''.join(uid.split('-'))
    year = instance.add_time.year
    month = instance.add_time.month
    day = instance.add_time.day
    path_name = 'uploads/image/{year}-{month}-{day}/{subuid}/{filename}'.format(
        year=year, month=month, day=day, subuid=subuid, filename=filename)
    return path_name


class ImageMeta(models.Model):
    image = models.FileField(upload_to=artical_image_path, verbose_name="artical_image", null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='上传者', null=True, blank=True, on_delete=models.PROTECT)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = ' 文章图片'
        verbose_name_plural = verbose_name
        ordering = ('modified_time',)

    def __str__(self):
        return self.image.name


@receiver(pre_delete, sender=ImageMeta)
def ImageMeta_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)
