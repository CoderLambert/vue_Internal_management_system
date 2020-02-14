# -*- coding: utf-8 -*-

import django_filters
from .models import RomImageFile

class RomImagesFilter(django_filters.rest_framework.FilterSet):
    """
    Rom的过滤类
    """
    class Meta:
        model = RomImageFile
        fields = ['project','user']
