# Generated by Django 3.0.2 on 2020-05-13 01:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0028_auto_20200503_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='romimagefile',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 1, 2, 54, 554199, tzinfo=utc), verbose_name='添加时间'),
        ),
    ]
