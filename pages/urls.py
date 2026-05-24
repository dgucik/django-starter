from django.urls import path

from pages.views import HomePageView, AboutPageView, LoginPageView, TriggerDelayView, PositionsPartialView, PositionView

urlpatterns = [
        path("login/", LoginPageView.as_view(), name="login"),
        path("", HomePageView.as_view(), name="home"),
        path("about/", AboutPageView.as_view(), name="about"),
        path("trigger_delay/", TriggerDelayView.as_view(), name="trigger_delay"),
        path("positions/", PositionsPartialView.as_view(), name="positions-partial"),
        path("positions/row/", PositionView.as_view(), name="positions"),
    ]