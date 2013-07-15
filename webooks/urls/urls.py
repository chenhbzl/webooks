# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from webooks.utils import const
from webooks.views.books import BookDetailView
from webooks.views.images import pil_image

urlpatterns = patterns('',
    url(r'^image/$', pil_image, name="auto_image"),
    url(r'^books/%s/$' %const.URL_ID, BookDetailView.as_view(), name="book_detail"),
)

urlpatterns = format_suffix_patterns(urlpatterns)