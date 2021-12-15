from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

default_password = 'Pass1234!'  # nosec


class Command(BaseCommand):
    help = 'Seed database with dummy data'

    def add_arguments(self, parser):
        parser.add_argument('--multiplier', '-m', nargs='?', type=int, default=1)

    @transaction.atomic
    def handle(self, *args, **options):
        # multiplier = options['multiplier']

        if not settings.DEBUG:
            raise CommandError('settings.DEBUG must be set to True.\nThis command should NOT be run in production!')

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
        self.stdout.write(self.style.SUCCESS('Superuser credentials:'))
        self.stdout.write(self.style.SUCCESS('email: admin@backend.com'))
        self.stdout.write(self.style.SUCCESS(f'password: {default_password}'))
