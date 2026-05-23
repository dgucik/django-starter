from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from config import settings
from django.urls import include

def get_urls():
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("pages.urls")),
    ]

    if settings.DEBUG:
        import debug_toolbar
        urlpatterns += [
            path(
            "__errors__/400/",
            TemplateView.as_view(template_name="errors/400.html"),
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "__errors__/403/",
            TemplateView.as_view(template_name="errors/403.html"),
            kwargs={"exception": Exception("Permission Denied.")},
        ),
        path(
            "__errors__/404/",
            TemplateView.as_view(template_name="errors/404.html"),
            kwargs={"exception": Exception("Page not Found.")},
        ),
        path(
            "__errors__/500/",
            TemplateView.as_view(template_name="errors/500.html"),
            kwargs={"exception": Exception("Internal Server Error.")},
            ),
        path("__debug__/", include(debug_toolbar.urls)),
        ]
    return urlpatterns

urlpatterns = get_urls()
