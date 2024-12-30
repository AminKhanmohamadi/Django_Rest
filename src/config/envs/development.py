from .common import *

ALLOWED_HOSTS = ['*']

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

# LOGGING = {
#     'version': 1,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#         },
#     },
#     'root':{
#         'handlers': ['console'],
#     }
# }