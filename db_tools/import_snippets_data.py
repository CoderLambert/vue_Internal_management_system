# -*- coding: utf-8 -*-
__author__ = 'bobby'

#独立使用django的model
import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Basilisk.settings")

import django
django.setup()

from snippets.models import Snippet

from .data.snippet_data import row_data

for snipet_item in row_data:
    snippet = Snippet()
    snippet.code = snipet_item['code']
    snippet.title = snipet_item['title']
    snippet.linenos = snipet_item['linenos']
    snippet.language = snipet_item['language']
    snippet.style = snipet_item['style']
    snippet.save()


