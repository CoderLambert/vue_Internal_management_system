# -*- coding: utf-8 -*-

import django_filters
from .models import Articale, Note,ArticleType

class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass

class ArticalFilter(django_filters.rest_framework.FilterSet):
    """
    Rom的过滤类
    """
    types = NumberInFilter(field_name='types', lookup_expr='in')

    class Meta:
        model = Articale
        fields = [ 'original','note','browse_num','user','types']

class NoteFilter(django_filters.rest_framework.FilterSet):
    """
    Rom的过滤类
    """
    class Meta:
        model = Note
        fields = [ 'id']


class ArticleTypeFilter(django_filters.rest_framework.FilterSet):
    """
    Rom的过滤类
    """

    class Meta:
        model = ArticleType
        fields = [ 'id',]