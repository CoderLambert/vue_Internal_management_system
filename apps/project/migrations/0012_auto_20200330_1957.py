# Generated by Django 3.0.2 on 2020-03-30 11:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20200330_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='romimagefile',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 30, 11, 57, 16, 911419, tzinfo=utc), verbose_name='添加时间'),
        ),
    ]