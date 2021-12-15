# pylint: disable=W0614
from .base import *  # pylint: disable=wildcard-import

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

DEBUG = True

INTERNAL_IPS += ['172.16.238.1']

JWT_AUTH_SECURE = False
