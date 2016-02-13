#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bruno Oliveira'
AUTHOR_EMAIL = u'nicoddemus@gmail.com'
SITENAME = u'Midnight Coding'
SITEURL = ''
SITESUBTITLE = 'Sleeping is for the weak'
DISPLAY_PAGES_ON_MENU = False

FILENAME_METADATA = r'(?P<slug>.*)'

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

ARTICLE_URL = 'articles/{slug}'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ('_src', '.git')

OUTPUT_PATH = '../'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
MENUITEMS = [
    ('Projects', '/pages/projects/'),
    ('About', '/pages/about/'),
]
LINKS = []

# Social widget
SOCIAL = [('GitHub', 'https://github.com/nicoddemus')]

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['x:\\pelican-plugins']
PLUGINS = ['gravatar']

THEME = 'blueidea'

PATH = 'content'
STATIC_PATHS = [
    'favicon.ico',
    'static',
]

import shutil
shutil.copy('favicon.ico', OUTPUT_PATH)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

