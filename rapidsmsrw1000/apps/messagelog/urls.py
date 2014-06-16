#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

# from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$',
        views.message_log,
        name="message_log"))
