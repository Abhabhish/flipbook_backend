# -*- coding: utf-8 -*-
# from django.conf.urls import 
from django.urls import re_path,path

from django.views.generic import TemplateView
from flipbook.views import flipbook
from . import views

urlpatterns = [
    re_path(r'^$', flipbook, name='flipbook'),
    re_path(r'^viewer.html$', TemplateView.as_view(template_name="viewer.html", content_type="text/html"), name="viewer"),
    re_path(r'viewer/',views.viewer,name='viewer'),
]
