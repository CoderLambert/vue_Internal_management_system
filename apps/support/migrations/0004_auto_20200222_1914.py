# Generated by Django 3.0.2 on 2020-02-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_auto_20200222_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloundresource',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000, null=True, verbose_name='文件描述'),
        ),
    ]
