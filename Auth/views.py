from django.shortcuts import render
from allauth.account import views as allauth_views

# authentication Views

class CustomAccountInactiveView(allauth_views.AccountInactiveView):
    template_name = 'auth/authentication/account_inactive.html'

class CustomLoginView(allauth_views.LoginView):
    template_name = 'auth/authentication/login.html'

class CustomLogoutView(allauth_views.LogoutView):
    template_name = 'auth/authentication/logout.html'

class CustomSignupView(allauth_views.SignupView):
    template_name = 'auth/authentication/signup.html'

# Email Views

class CustomConfirmEmailView(allauth_views.ConfirmEmailView):
    template_name = 'auth/email/confirm_email.html'

class CustomEmailVerificationSentView(allauth_views.EmailVerificationSentView):
    template_name = 'auth/email/email_verification_sent.html'

class CustomEmailView(allauth_views.EmailView):
    template_name = 'auth/email/email.html'

# Password Views

class CustomPasswordChangeView(allauth_views.PasswordChangeView):
    template_name = 'auth/password/password_change.html'

class CustomPasswordResetDoneView(allauth_views.PasswordResetDoneView):
    template_name = 'auth/password/password_reset_done.html'

class CustomPasswordResetFromKeyDoneView(allauth_views.PasswordResetFromKeyDoneView):
    template_name = 'auth/password/password_reset_from_key_done.html'

class CustomPasswordResetFromKeyView(allauth_views.PasswordResetFromKeyView):
    template_name = 'auth/password/password_reset_from_key.html'

class CustomPasswordResetView(allauth_views.PasswordResetView):
    template_name = 'auth/password/password_reset.html'

class CustomPasswordSetView(allauth_views.PasswordSetView):
    template_name = 'auth/password/password_set.html'