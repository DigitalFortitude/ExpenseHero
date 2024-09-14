from .views import (RegistrationView, UsernameValidationView, EmailValidationView,
                    VerificationView, LoginView, LogoutView, RequestPasswordResetEmail,
                    UserPasswordReset, PasswordValidation)
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate-email'),
    path('validate-password', csrf_exempt(PasswordValidation.as_view()), name='validate-password'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('set-new-password/<uidb64>/<token>', UserPasswordReset.as_view(), name='reset-user-password'),
    path('request-password-link', RequestPasswordResetEmail.as_view(), name='reset-password')
]
