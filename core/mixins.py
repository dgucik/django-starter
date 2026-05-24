from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


class HtmxFormMixin:
    success_url = None

    def form_valid(self, _form):
        response = HttpResponse(status=204)
        response["HX-Redirect"] = reverse(self.success_url)
        return response
