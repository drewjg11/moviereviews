# pylint: disable=W0614

from .base import *  # pylint: disable=wildcard-import

DEBUG = False

DEFAULT_FROM_EMAIL = env.str('DJANGO_DEFAULT_FROM_EMAIL', 'noreply@XXXXXXX.com')

JWT_AUTH_SECURE = True
