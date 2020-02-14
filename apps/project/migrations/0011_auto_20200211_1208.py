# Generated by Django 3.0.2 on 2020-02-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20200210_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machineinfo',
            name='name',
        ),
        migrations.AlterField(
            model_name='machineinfo',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='机器信息描述'),
        ),
    ]