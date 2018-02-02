from cookify.settings.base import *

__author__ = 'William'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': SETTINGS['production']
}


