# Generated by Django 3.0.2 on 2020-03-13 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_machineinfo_add_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machineinfo',
            old_name='setting_time',
            new_name='start_time',
        ),
    ]
