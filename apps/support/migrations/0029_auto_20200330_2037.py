# Generated by Django 3.0.2 on 2020-03-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0028_auto_20200330_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
    ]
