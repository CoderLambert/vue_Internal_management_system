# Generated by Django 3.0.2 on 2020-02-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0009_auto_20200223_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloundresource',
            name='description',
            field=models.TextField(blank=True, default='', max_length=3000, null=True, verbose_name='文件描述'),
        ),
    ]
