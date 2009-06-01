#!/usr/bin/env python
# -*- coding: UTF-8 -*-
DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'db.sqlite'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

URCHIN_ID = ''

MEDIA_ROOT = './../../static'
MEDIA_URL = '/static/'
FILEBROWSER_URL_FILEBROWSER_MEDIA = MEDIA_URL + 'filebrowser/'
FILEBROWSER_URL_WWW = MEDIA_URL + 'uploads/'

ADMIN_MEDIA_PREFIX = '/media/'

TINYMCE_JS_URL = '%stiny_mce/tiny_mce.js' % MEDIA_URL
TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, 'tiny_mce')

SYNTAXHIGHLIGHTER_JS_URL = MEDIA_URL + 'syntaxhighlighter/'

TEMPLATE_DIRS = (
        './../../templates/diy_sample/',
        './../../templates/default/',
)

BLOG_CONFIG = {'title': u'DPress',
        'sub_title': u'Blog Sub Title',
        'blog_simple_descn': u'Blog Simple Descn',
        'End': ''}
