# Generated by Django 3.0.2 on 2020-02-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0006_auto_20200223_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloundresource',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='资源名'),
        ),
        migrations.AlterField(
            model_name='resourcetype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='资源名'),
        ),
        migrations.AlterField(
            model_name='websitelink',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='网站名'),
        ),
        migrations.AlterField(
            model_name='websitetype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='网站类型'),
        ),
    ]
