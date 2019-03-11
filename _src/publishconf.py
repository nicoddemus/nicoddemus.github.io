#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.nicoddemus.dev'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = 'category/{slug}/atom.xml'
TAG_FEED_ATOM = 'tag/{slug}/atom.xml'

# Following items are often useful when publishing
DISQUS_SITENAME = "midnightcoding"
GOOGLE_ANALYTICS = "UA-43463457-1"
