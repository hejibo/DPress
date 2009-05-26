from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    # Example:
    (r'^$', views.index),

)

from django.views.generic.simple import direct_to_template

urlpatterns += patterns('',
    # Example:
    (r'^test/base/$', direct_to_template, {'template': 'dpress/base.html'}),
    (r'^test/ext_base/$', direct_to_template, {'template': 'dpress/ext_base.html'}),
    (r'^test/$', direct_to_template, {'template': 'dpress/index.html'}),
)
