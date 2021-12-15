import json
import os
import sys

ENVIRONMENT_CONFIGS = {
    'main': {
        'environment': 'MAIN',
        'debug_level': 'INFO',
        'zappa_target': 'main',
    },
    'develop': {
        'environment': 'DEVELOP',
        'debug_level': 'DEBUG',
        'zappa_target': 'develop',
    },
    'stage': {
        'environment': 'STAGE',
        'debug_level': 'INFO',
        'zappa_target': 'develop',
    }
}


def handler():
    zappa_settings = json.load(open('src/zappa_settings.json', 'r'))

    environment_config = ENVIRONMENT_CONFIGS[sys.argv[1]]
    environment = environment_config['environment']

    zappa_settings[environment_config['zappa_target']]['environment_variables'] = {
        'AWS_ACCESS_KEY_ID': os.environ.get('AWS_ACCESS_KEY_ID'),
        'AWS_SECRET_ACCESS_KEY': os.environ.get('AWS_SECRET_ACCESS_KEY'),
        'DJANGO_EMAIL_URL': os.environ.get('DJANGO_EMAIL_URL'),
        'ROLLBAR_POST_SERVER_ITEM_ACCESS_TOKEN': os.environ.get('ROLLBAR_POST_SERVER_ITEM_ACCESS_TOKEN'),

        'DJANGO_DATABASE_URL': os.environ.get(f'{environment}_DJANGO_DATABASE_URL'),
        'DJANGO_SECRET_KEY': os.environ.get(f'{environment}_DJANGO_SECRET_KEY'),
        'DJANGO_LOG_LEVEL': environment_config['debug_level']
    }

    fp = open('src/zappa_settings.json', 'w')
    json.dump(zappa_settings, fp, indent=2)
    fp.close()


if __name__ == '__main__':
    handler()
