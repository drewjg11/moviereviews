from dj_rest_auth.serializers import PasswordResetSerializer
from django.conf import settings


class P3PasswordResetSerializer(PasswordResetSerializer):
    def get_email_options(self):
        return {
            'html_email_template_name': 'registration/password_reset_email.html',
        }

    # def save(self):
    #     request = self.context.get('request')
    #     opts = {
    #         'use_https': request.is_secure(),
    #         'from_email': 'example@yourdomain.com',
    #         'request': request,
    #         'email_template_name': 'password_reset_email.html'
    #     }
    #
    #     opts.update(self.get_email_options())
    #     self.reset_form.save(**opts)

    # def get_email_options(self):
    #     request = self.context.get('request')
    #     return {
    #         'email_template_name': 'password_reset_email.html',
    #         'html_email_template_name': 'password_reset_email.html',
    #         'extra_email_context': {
    #             'BASE_URL': f'{request.scheme}://{request.get_host()}',
    #             'frontend_url': settings.FRONTEND_URL
    #         }
    #     }
