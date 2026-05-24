from django.urls import path

from pages.views import HomePageView, AboutPageView, LoginPageView, TriggerDelayView, PositionsListView, PositionsSaveView, PositionRowView

urlpatterns = [
        path("login/", LoginPageView.as_view(), name="login"),
        path("", HomePageView.as_view(), name="home"),
        path("about/", AboutPageView.as_view(), name="about"),
        path("trigger_delay/", TriggerDelayView.as_view(), name="trigger_delay"),
        path("positions/", PositionsListView.as_view(), name="positions"),
        path("positions/save/", PositionsSaveView.as_view(), name="positions-save"),
        path("positions/row/", PositionRowView.as_view(), name="positions-row"),
    ]