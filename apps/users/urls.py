
from apps.users.views import LoginFormView
from django.contrib.auth.views import LogoutView
from django.urls import path

app_name = 'users'

urlpatterns= [
    path("login-form/", LoginFormView.as_view(), name="login-form"),
    path("logout-action/", LogoutView.as_view(), name="logout-action"),
]