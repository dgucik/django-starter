from django.shortcuts import render
from http import HTTPStatus

class HtmxRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.headers.get("HX-Request"):
            return self.handle_no_htmx()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_htmx(self):
        return render(self.request, "errors/404.html", status=HTTPStatus.NOT_FOUND)