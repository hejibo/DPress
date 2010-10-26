#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

#cp -R /path/to/grappelli/media /path/to/your/admin/media
urlpatterns = patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    #(r'^tinymce/', include('tinymce.urls')),

    #(r'^comments/', include('comments_urls')),
    #(r'^', include('dpress.urls')),

    url(r'^admin_tools/', include('admin_tools.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
