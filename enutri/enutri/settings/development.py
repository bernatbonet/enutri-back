import os
from .base import (
    BASE_DIR, FRONTEND_DIR, INSTALLED_APPS, MIDDLEWARE
)


INSTALLED_APPS += [
    'debug_toolbar', 
    'webpack_loader',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR+'/databases', 'db.sqlite3'),
    }
}

INTERNAL_IP = [
    '127.0.0.1',
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': os.getenv('DJANGO_DEBUG') ,
        'BUNDLE_DIR_NAME': '/bundles/',
        'STATS_FILE': os.path.join(FRONTEND_DIR, 'webpack-stats.json'),
    }
}