from .base import *

INSTALLED_APPS += [
    'debug_toolbar', 
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