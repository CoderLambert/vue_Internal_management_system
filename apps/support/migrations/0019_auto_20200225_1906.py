# Generated by Django 3.0.2 on 2020-02-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0018_auto_20200225_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitetype',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='网站类型'),
        ),
    ]
