from django.views import View
from django.shortcuts import render
from abc import ABC

class PageView(ABC, View):
    template_name = None

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)