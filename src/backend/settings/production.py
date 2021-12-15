# pylint: disable=unused-wildcard-import

import rollbar

from .base import *  # pylint: disable=wildcard-import

CORS_ALLOWED_ORIGINS += [
    'https://api.p3mgnt.com',
    'https://p3mgnt.com',
    'https://static.p3mgnt.com',
]

DEBUG = False

DEFAULT_FROM_EMAIL = env.str('DJANGO_DEFAULT_FROM_EMAIL', 'noreply@XXXXXXX.com')

ENVIRONMENT = 'production'

FRONTEND_URL = 'https://p3mgnt.com'

JWT_AUTH_SECURE = True

ROLLBAR['environment'] = 'production'
rollbar.init(**ROLLBAR)
