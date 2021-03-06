# Generated by Django 3.0.2 on 2020-02-22 13:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0004_auto_20200222_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebSiteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='网站类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '资源类型',
                'verbose_name_plural': '资源类型',
                'ordering': ('add_time',),
            },
        ),
        migrations.CreateModel(
            name='WebSiteLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='网站名')),
                ('url', models.URLField(blank=True, default='', max_length=500, null=True, verbose_name='网站地址')),
                ('description', models.TextField(blank=True, default='', max_length=1000, null=True, verbose_name='网站描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='添加人员')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='support.WebSiteType', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '网站',
                'verbose_name_plural': '网站',
                'ordering': ('add_time',),
            },
        ),
    ]
