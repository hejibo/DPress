#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^%s' % settings.PREFIX_URL, include('dpress.urls')),
)
