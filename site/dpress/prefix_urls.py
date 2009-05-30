#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^', include('dpress.urls')),
)
