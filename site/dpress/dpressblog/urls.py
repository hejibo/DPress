from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    # Example:
    url(r'^$', views.index, name='dpress_index'),
    url(r'^tags/(?P<tag>[-\w]+)/$', views.index, name='dpress_tag'),
    url(r'^post/(?P<username>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[-\w]+)/$', 
        views.post, name='dpress_post'),

)

from django.views.generic.simple import direct_to_template

urlpatterns += patterns('',
    # Example:
    (r'^test/base/$', direct_to_template, {'template': 'dpress/base.html'}),
    (r'^test/ext_base/$', direct_to_template, {'template': 'dpress/ext_base.html'}),
    (r'^test/$', direct_to_template, {'template': 'dpress/index.html'}),
)
