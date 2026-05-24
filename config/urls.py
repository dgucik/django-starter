from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import render

from config import settings
from django.urls import include

def custom_400(request, exception):
    return render(request, 'errors/400.html', status=400)

def custom_403(request, exception):
    return render(request, 'errors/403.html', status=403)

def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500(request):
    return render(request, 'errors/500.html', status=500)

def get_urls():
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("pages.urls")),
        path("users/", include("apps.users.urls")),
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

handler400 = custom_400
handler403 = custom_403
handler404 = custom_404
handler500 = custom_500