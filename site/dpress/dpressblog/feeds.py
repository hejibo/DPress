from django.contrib.syndication.feeds import Feed
from models import Post
from django.conf import settings

class LatestDPressPostFeed(Feed):
    title = settings.BLOG_CONFIG['title']
    link = settings.BLOG_URL
    description_template = 'dpress/feeds/description.html'
    description = settings.BLOG_CONFIG['blog_simple_descn']

    def items(self):
        return Post.objects.filter(status=2).order_by("-publish")[:10]

    def item_pubdate(self, item):
        return item.publish
