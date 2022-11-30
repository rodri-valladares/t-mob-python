from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_local',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

STATIC_URL = '/static/'