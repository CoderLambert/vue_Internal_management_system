# Generated by Django 3.0.2 on 2020-04-10 01:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_auto_20200409_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='romimagefile',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 1, 32, 46, 702301, tzinfo=utc), verbose_name='添加时间'),
        ),
    ]
