# Generated by Django 3.0.2 on 2020-02-10 06:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0005_romimagefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='备注')),
                ('ip', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='IP 地址')),
                ('svn', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='SVN 地址')),
                ('build', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='机器描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.Project', verbose_name='所属项目')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='成员')),
            ],
            options={
                'verbose_name': 'MachineInfo',
                'verbose_name_plural': 'MachineInfo',
                'ordering': ('add_time',),
            },
        ),
    ]