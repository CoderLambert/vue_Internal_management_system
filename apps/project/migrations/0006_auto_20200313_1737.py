# Generated by Django 3.0.2 on 2020-03-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20200313_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machineinfo',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='machineinfo',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='起始时间'),
        ),
    ]
