import os
import random
import sys

from shutil import copyfile


def handler():
    print('This command should only be ran once when the repository is first downloaded on a developer\'s machine.')
    response = input('Would you like to continue? (y): ')
    if not response.lower() == 'y':
        print('\'y\' not provided. Exiting')
        sys.exit()
    project_name = os.path.basename(os.getcwd())

    # Checks to make sure project is pristine
    if os.path.exists(f'src/{project_name}/settings/.env'):
        print('It does not appear that this is a new project.')
        sys.exit(1)

    # Rename .env file
    copyfile(f'config/example.env', f'src/{project_name}/settings/.env')

    # Generate and populate secret key.
    # Hard code first letter to ensure it doesnt start with a $ (limitation of django-environ)
    secret_key = 'f' + ''.join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(49)])
    with open(f'src/{project_name}/settings/.env') as fp:
        content = fp.read().replace('DJANGO_SECRET_KEY=', f'DJANGO_SECRET_KEY={secret_key}')
    with open(f'src/{project_name}/settings/.env', 'w') as fp:
        fp.write(content)


if __name__ == '__main__':
    handler()
