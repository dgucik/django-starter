
from apps.users.views import LoginActionView, LoginFormPartialView
from django.contrib.auth.views import LogoutView
from django.urls import path

app_name = 'users'

urlpatterns= [
    path("login-form-partial/", LoginFormPartialView.as_view(), name="login-form-partial"),
    path("login-action/", LoginActionView.as_view(), name="login-action"),
    path("logout-action/", LogoutView.as_view(), name="logout-action"),
]