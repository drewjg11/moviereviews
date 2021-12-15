# pylint: disable=W0614./
import rollbar

from .base import *  # pylint: disable=wildcard-import

ALLOWED_HOSTS = ['.execute-api.us-east-1.amazonaws.com', '.XXXXXXX.com']

CORS_ALLOWED_ORIGINS += [
    'https://api.develop.p3mgnt.com',
    'https://frontend.develop.p3mgnt.com',
    'https://static.develop.p3mgnt.com',
]

DEBUG = True

DEFAULT_FROM_EMAIL = env.str('DJANGO_DEFAULT_FROM_EMAIL', 'noreply@XXXXXXX.com')

ENVIRONMENT = 'develop'

FRONTEND_URL = 'https://frontend.develop.XXXXXXXX.com'

INSTALLED_APPS += ['django_extensions', 'debug_toolbar']

JWT_AUTH_SECURE = False

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    *REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'],
    'rest_framework.renderers.BrowsableAPIRenderer'
)

ROLLBAR['environment'] = 'develop'
rollbar.init(**ROLLBAR)

STATIC_URL = env.str('DJANGO_STATIC_URL', 'https://static.develop.XXXXXXX.com/')
