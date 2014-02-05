from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

if DEBUG is False:
    ALLOWED_HOSTS = ('127.0.0.1', )

INSTALLED_APPS += ('debug_toolbar',)
