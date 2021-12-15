# pylint: disable=W0614
import rollbar

from .base import *  # pylint: disable=wildcard-import

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

CORS_ALLOWED_ORIGINS += [
    "http://localhost:8000",
    "http://localhost:3000",
    'https://editor.swagger.io'
]

DEBUG = True

DEFAULT_FROM_EMAIL = env.str('DJANGO_DEFAULT_FROM_EMAIL', 'noreply@XXXXXXX.com')

ENVIRONMENT = 'local'

FRONTEND_URL = 'http://localhost:3000/'

INSTALLED_APPS += ['django_extensions', 'debug_toolbar']

INTERNAL_IPS += ['172.16.238.1']

JWT_AUTH_SECURE = False

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = (
    *REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'],
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication',
)

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    *REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'],
    'rest_framework.renderers.BrowsableAPIRenderer'
)

ROLLBAR['environment'] = 'local'
rollbar.init(**ROLLBAR)
