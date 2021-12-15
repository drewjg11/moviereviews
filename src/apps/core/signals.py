from allauth.account.signals import email_confirmed
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string


@receiver(email_confirmed)
def send_email_confirmed_email(request, email_address, **kwargs):
    context = {}
    html_template = render_to_string('account/email/welcome_message.html', context, request)
    txt_template = render_to_string('account/email/welcome_message.txt', context, request)
    subject = 'Welcome to P3'

    msg = EmailMultiAlternatives(subject=subject, body=txt_template, to=[email_address.email])
    msg.attach_alternative(html_template, "text/html")
    msg.send()
