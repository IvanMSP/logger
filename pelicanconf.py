#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ivan Lopez'
SITENAME = 'Logger'
SITEURL = ''

# Theme
# FAVICON = "favicon.ico"
THEME = '/home/bawbamgeek/Documents/Personal_proyects/LoggerMe/env/lib/python3.8/site-packages/pelican/themes/attila'
HOME_COVER = 'https://i.imgur.com/4HWzHSf.jpg'
HEADER_COVERS_BY_TAG = {}
HEADER_COVERS_BY_CATEGORY = {}
HOME_COLOR = 'black'
COLOR_SCHEME_CSS = 'darkly.css'

# Content
PATH = 'content'
TIMEZONE = 'America/Mexico_City'
DEFAULT_LANG = 'es'
DEFAULT_PAGINATION = 5

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/BawbamGeek'),
        ('linkedIn', 'https://www.linkedin.com/in/ivanlopz/'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
AUTHORS_BIO = {
  "ivan": {
    "name": "Ivan López",
    "cover": "https://i.imgur.com/4HWzHSf.jpg",
    "image": "https://i.imgur.com/gQUjlR5.png",
    "website": "https://bawbamgeek.com",
    "twitter": "BawbamGeek",
    "linkedin": "ivanlopz",
    "location": "México",
    "bio": "Backend Developer."
  }
}

STATIC_PATHS = [
    'assets',
    ]

EXTRA_PATH_METADATA = {
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'},
}
