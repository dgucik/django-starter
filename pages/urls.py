from django.urls import path
from django.contrib.auth.views import LogoutView

from pages.views import HomePageView, AboutPageView, LoginPageView

def get_urls():
    return [
        path("login/", LoginPageView.as_view(), name="login"),
        path("logout/", LogoutView.as_view(), name="logout"),
        path("", HomePageView.as_view(), name="home"),
        path("about/", AboutPageView.as_view(), name="about"),
    ]

urlpatterns = get_urls()