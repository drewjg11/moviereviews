import logging

from django.apps import apps
from django.test import TestCase

from apps.core.apps import CoreConfig

logger = logging.getLogger(__name__)


class TestApps(TestCase):
    def test_app_has_correct_name(self):
        assert CoreConfig.name == 'apps.core'
        assert apps.get_app_config('core').name == 'apps.core'
