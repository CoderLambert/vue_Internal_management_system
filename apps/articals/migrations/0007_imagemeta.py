# Generated by Django 3.0.2 on 2020-04-18 12:56

import articals.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articals', '0006_articale_browse_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to=articals.models.artical_image_path, verbose_name='artical_image')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='上传者')),
            ],
            options={
                'verbose_name': ' 文章图片',
                'verbose_name_plural': ' 文章图片',
                'ordering': ('modified_time',),
            },
        ),
    ]