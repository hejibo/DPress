from django.conf.urls.defaults import *
from django.contrib.comments.views import comments
from django.contrib.comments.views import moderation

urlpatterns = patterns('django.contrib.comments.views',
    url(r'^post/$',          comments.post_comment,       name='comments-post-comment'),
    url(r'^posted/$',        comments.comment_done,       name='comments-comment-done'),
)

urlpatterns += patterns('',
    url(r'^cr/(\d+)/(.+)/$', 'django.views.defaults.shortcut', name='comments-url-redirect'),
)

