# Generated by Django 3.0.2 on 2020-02-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_machineinfo_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machineinfo',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='machineinfo',
            name='password',
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='BMC_ip',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='BMC IP 地址'),
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='Host_ip',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Host IP 地址'),
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='web_password',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Web 密码'),
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='web_username',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Web 用户名'),
        ),
    ]