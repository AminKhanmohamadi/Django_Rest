from .common import *

INSTALLED_APPS = [
    'daphne',
    'drf_spectacular',
]+ INSTALLED_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Django_Rest',
        'USER': 'postgres',
        'PASSWORD': 'aminkhm',
        'HOST': 'db',
        'PORT': '5432',
    }
}