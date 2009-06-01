# Django settings for dpress project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'db.sqlite'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'#'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'#'en-us'

SITE_ID = 1

URCHIN_ID = ''

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = './../../static'
#'E:/soho/dpress_svn/trunk/static'


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'
FILEBROWSER_URL_FILEBROWSER_MEDIA = MEDIA_URL + 'filebrowser/'
FILEBROWSER_URL_WWW = MEDIA_URL + 'uploads/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

TINYMCE_JS_URL = '%stiny_mce/tiny_mce.js' % MEDIA_URL
TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, 'tiny_mce')

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#(886ewc)@$jz7opzk5@q+4xx3ged()rvmg0_d=dqq*t)*%t+w'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'dpress.prefix_urls'

TEMPLATE_DIRS = (
        './../../templates/diy_sample/',
        './../../templates/default/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",

    "dpress.dpressblog.context_processors.common",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.comments',
    'django.contrib.syndication',

    'tinymce',
    'filebrowser',
    'tagging',

    'dpress.dpressblog',

    #'django_evolution',
)

BLOG_CONFIG = {'title': u'DPress',
        'sub_title': u'Blog Sub Title',
        'blog_simple_descn': u'Blog Simple Descn',
        'End': ''}

try:
    from settings_local import *
except Exception, e:
    pass
