# Generated by Django 3.0.2 on 2020-04-10 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articals', '0004_articale_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articale',
            old_name='author',
            new_name='user',
        ),
    ]
