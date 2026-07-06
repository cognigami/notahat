#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ricardo Olenewa'
SITENAME = u'It\'s Not a Hat'
SITETITLE = u'A blog documenting a translation of Antoine de St. Exupery\'s The Little Prince'
# If using GitHub Pages, set the SITEURL parameter to be the repo name.
# Otherwise, leave as null.
# SITEURL = 'notahat'

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment these to test the feeds
# FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DEFAULT_PAGINATION = 2

PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# My own defaults
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['eric_extensions', 'neighbors', 'sitemap'] #, 'yuicompressor']

THEME = 'theme'
LOGO = 'images/notahat_small.png'

DEFAULT_CATEGORY = 'Dross'

DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'tags']

SITEMAP = {
    'format': 'xml',
    'exclude': ['tags/', 'author/', 'categories/']
}

YUICOMPRESSOR_EXECUTABLE = 'yui-compressor'

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
AUTHOR_SAVE_AS = ''
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'

ARCHIVES_SAVE_AS = 'posts/index.html'
ARCHIVES_URL = 'posts/'
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORIES_URL = 'categories'
TAGS_SAVE_AS = 'tags/index.html'
TAGS_URL = 'tags/'

STATIC_PATHS = [
    'images',
    'static',
    'fonts'
    ]

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
    }

# Theme extras
MENUITEMS = [
  ('Vault', 'posts/'),
]

SITEMETA = "It's Not a Hat"
