# Generated by Django 3.0.2 on 2020-02-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_machineinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='machineinfo',
            name='password',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='密码'),
        ),
    ]