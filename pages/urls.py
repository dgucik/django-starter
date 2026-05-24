from django.urls import path

from pages.views import HomePageView, AboutPageView, LoginPageView

urlpatterns = [
        path("login/", LoginPageView.as_view(), name="login"),    
        path("", HomePageView.as_view(), name="home"),
        path("about/", AboutPageView.as_view(), name="about"),
    ]