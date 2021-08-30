#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ivan Lopez'
SITENAME = 'Logger'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/myprofile'),
        ('github', 'https://github.com/myprofile'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/home/bawbamgeek/Documents/Personal_proyects/LoggerMe/env/lib/python3.8/site-packages/pelican/themes/attila'
HOME_COVER = 'https://images.pexels.com/photos/4688545/pexels-photo-4688545.jpeg'
HEADER_COVERS_BY_TAG = {'food': '/images/food.png', 'drinks':'/images/orange-juice.png'}
HEADER_COVERS_BY_CATEGORY = {'food': '/images/junkie-stuff.png'}
HOME_COLOR = 'black'
COLOR_SCHEME_CSS = 'darkly.css'

STATIC_PATHS = [
    'assets',
    ]

EXTRA_PATH_METADATA = {
    'assets/favicon.ico': {'path': 'favicon.ico'},
}
