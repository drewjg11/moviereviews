from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('google/login/', csrf_exempt(views.GoogleLogin.as_view()), name='google_login'),
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('register/send-email-verification/', views.resend_email_verification_email),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/email/password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
]
