# Generated by Django 3.0.2 on 2020-04-13 03:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_auto_20200410_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='romimagefile',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 3, 15, 12, 522485, tzinfo=utc), verbose_name='添加时间'),
        ),
    ]
