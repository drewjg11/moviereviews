import logging

from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

logger = logging.getLogger(__name__)


class AccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        context['frontend_url'] = settings.FRONTEND_URL
        context['BASE_URL'] = f'{self.request.scheme}://{self.request.get_host()}'
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
