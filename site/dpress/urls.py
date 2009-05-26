#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIR}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),

    (r'^', include('dpress.dpressblog.urls')),
)
