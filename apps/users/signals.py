# -*- coding: utf-8 -*-
import re
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()
pbkdf2_sha256_pattern = re.compile(r'pbkdf2_sha256\$180000\$')
@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        # if pbkdf2_sha256_pattern.match(password) is None:
        instance.set_password(password)

        instance.save()
