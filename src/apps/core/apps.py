from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'apps.core'

    def ready(self):
        import apps.core.signals  # pylint: disable=C0415,W0611:

        super().ready()
