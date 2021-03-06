# Generated by Django 3.0.2 on 2020-04-22 07:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articals', '0007_imagemeta'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='分类名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='articals.ArticleType')),
            ],
            options={
                'verbose_name': '文章分类标签',
                'verbose_name_plural': '文章分类标签',
            },
        ),
    ]
