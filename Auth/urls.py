"""
URL configuration for projetecj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from Auth import views as auth_views

urlpatterns = [
    path('login/',auth_views.CustomLoginView.as_view(), name='account_login'),
    
    path('signup/',auth_views.CustomSignupView.as_view(), name='account_signup'),
    path('logout/',auth_views.CustomLogoutView.as_view(), name='account_logout'),
    path('password/change/',auth_views.CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('password/set/',auth_views.CustomPasswordSetView.as_view(), name='account_set_password'),
    path('password/reset/',auth_views.CustomPasswordResetView.as_view(), name='account_reset_password'),
    path('password/reset/done/',auth_views.CustomPasswordResetDoneView.as_view(), name='account_reset_password_done'),
    path('password/reset/key/',auth_views.CustomPasswordResetFromKeyView.as_view(), name='account_reset_password_from_key'),
    path('password/reset/key/done/',auth_views.CustomPasswordResetFromKeyDoneView.as_view(), name='account_reset_password_from_key_done'),
    path('email/',auth_views.CustomEmailView.as_view(), name='account_email'),
    path('email/sent/',auth_views.CustomEmailVerificationSentView.as_view(), name='account_email_verification_sent'),
    path('confirm-email/',auth_views.CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('inactive/',auth_views.CustomAccountInactiveView.as_view(), name='account_inactive'),

]
