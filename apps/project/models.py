import datetime
import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_init, pre_delete, post_save, post_init
from django.dispatch.dispatcher import receiver

# from django.core.mail import send_mail  # 引入模块

# Create your models here.
User = get_user_model()


def rom_path(instance, filename):
    uid = str(uuid.uuid4())
    subuid = ''.join(uid.split('-'))
    year = instance.add_time.year
    month = instance.add_time.month
    day = instance.add_time.day
    path_name = 'uploads/{project_name}/{year}-{month}-{day}/roms/{subuid}/{filename}'.format(
        project_name=instance.project.name, year=year, month=month, day=day, subuid=subuid, filename=filename)
    return path_name


def release_note_path(instance, filename):
    uid = str(uuid.uuid4())
    subuid = ''.join(uid.split('-'))
    year = instance.add_time.year
    month = instance.add_time.month
    day = instance.add_time.day
    path_name = 'uploads/{project_name}/{year}-{month}-{day}/release_note/{subuid}/{filename}'.format(
        project_name=instance.project.name, year=year, month=month, day=day, subuid=subuid, filename=filename)
    return path_name


class Project(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name="项目名")
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
    member = models.ManyToManyField(User, verbose_name=' 项目成员', null=True, blank=True)
    svn = models.CharField(max_length=500, verbose_name='SVN 地址', blank=True, null=True, default='')
    build = models.CharField(max_length=500, verbose_name='Build 脚本参数', blank=True, null=True, default='')

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name
        ordering = ('add_time',)

    def __str__(self):
        return self.name


class RomImageFile(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default='')
    url = models.FileField(upload_to=rom_path, verbose_name="镜像文件", null=True, blank=True)
    release_note = models.FileField(upload_to=release_note_path, verbose_name="releaseNote", null=True, blank=True)
    release_note_name = models.CharField(max_length=100, blank=True, null=True, default='')
    user = models.ForeignKey(User, verbose_name='上传用户', null=True, blank=True, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, verbose_name='所属项目', null=True, blank=True, on_delete=models.PROTECT)
    description = models.TextField(verbose_name='文件描述', null=True, blank=True, default='')
    add_time = models.DateTimeField(default=timezone.now(), verbose_name="添加时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    # TODO 添加逻辑删除
    class Meta:
        verbose_name = 'RomImage'
        verbose_name_plural = verbose_name
        ordering = ('add_time',)

        def __str__(self):
            return self.name


@receiver(pre_delete, sender=RomImageFile)
def rom_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.url.delete(False)
    instance.release_note.delete(False)


# @receiver(post_save, sender = RomImageFile)
# def rom_saved(sender, instance, **kwargs):
#     Subject = '镜像文件更新通知'
#     from_email = 'lizhi1@cancon.com.cn'
#     user_emails = User.objects.values('email')
#     target_mails = [user['email'] for user in user_emails]
#     if from_email in target_mails:
#         target_mails.remove(from_email)
#     message = instance.description
#     send_mail(Subject, message, from_email, target_mails)

STATUS_CHOICE = (
    (1, '空闲'),
    (2, '使用中(可查看,请勿操作)'),
    (3, '占用中,勿动'),
)


class MachineInfo(models.Model):
    BMC_ip = models.CharField(max_length=100, verbose_name='BMC IP 地址', blank=True, null=True, default='')
    Host_ip = models.CharField(max_length=100, verbose_name='Host IP 地址', blank=True, null=True, default='')
    web_username = models.CharField(max_length=100, verbose_name='Web 用户名', blank=True, null=True, default='admin')
    web_password = models.CharField(max_length=100, verbose_name='Web 密码', blank=True, null=True, default='admin')
    description = models.TextField(verbose_name='机器信息描述', null=True, blank=True, default='')
    user = models.ForeignKey(User, verbose_name='所有者', null=True, blank=True, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, verbose_name='所属项目', null=True, blank=True, on_delete=models.PROTECT)
    current_state = models.IntegerField(verbose_name='机器状态', choices=STATUS_CHOICE, default=1)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
    start_time = models.DateTimeField(verbose_name="起始时间", blank=True, null=True)
    end_time = models.DateTimeField(verbose_name="结束时间", blank=True, null=True)

    # TODO 添加逻辑删除
    class Meta:
        verbose_name = 'MachineInfo'
        verbose_name_plural = verbose_name

        # ordering = ('add_time',)

        def __str__(self):
            return self.name
