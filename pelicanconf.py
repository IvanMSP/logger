#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ivan Lopez'
SITENAME = 'Logger'
SITEURL = ''

# Theme
THEME = '/home/bawbamgeek/Documents/Personal_proyects/LoggerMe/env/lib/python3.8/site-packages/pelican/themes/attila'
HOME_COVER = 'https://images.pexels.com/photos/4688545/pexels-photo-4688545.jpeg'
HEADER_COVERS_BY_TAG = {}
HEADER_COVERS_BY_CATEGORY = {}
HOME_COLOR = 'black'
COLOR_SCHEME_CSS = 'darkly.css'

# Content
PATH = 'content'
TIMEZONE = 'America/Mexico_City'
DEFAULT_LANG = 'es'
DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/myprofile'),
        ('github', 'https://github.com/myprofile'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'assets',
    ]

EXTRA_PATH_METADATA = {
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'},
}
