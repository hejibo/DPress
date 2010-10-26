from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        self.children.append(modules.LinkList(
            title=_('Media Management'),
            css_classes=['column_1'],
            children=[
                {
                    'title': _('Django FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                    'description': 'Python programming language rocks !',
                    },
                ]
            ))

        self.children.append(modules.AppList(
            title=_('User...'),
            models=('django.contrib.auth.models.User',),
            css_classes=['column_1', 'collapse', 'open'],
        ))
        
        self.children.append(modules.AppList(
            title=_('Administration'),
            include_list=('django.contrib',),
            css_classes=['column_1', 'collapse', 'closed'],
        ))
        
        self.children.append(modules.AppList(
            title=_('Administration'),
            exclude_list=('django.contrib',),
            css_classes=['column_1', 'collapse', 'closed'],
        ))
        
