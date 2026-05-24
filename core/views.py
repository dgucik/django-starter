from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from abc import ABC, abstractmethod
from django.urls import reverse
from django.views.generic import FormView as DjangoFormView, TemplateView as DjangoTemplateView

class PageView(ABC, DjangoTemplateView):
    """
    Base view for full-page SSR rendering.

    Handles page composition and layout orchestration.
    """

    template_name = None

class FormView(ABC, DjangoFormView):
    """
    Base view for form lifecycle handling (GET + POST).

    Responsible for validation, errors, and submit flow.
    """

    template_name = None
    form_class = None
    success_url = None

    def form_valid(self, _form):
        response = HttpResponse(status=204)
        response["HX-Redirect"] = reverse(self.success_url)
        return response

    def form_invalid(self, form):
        return render(self.request, self.template_name, {"form": form}, status=400)

class PartialView(ABC, View):
    """
    Base view for rendering backend-driven UI fragments.

    Returns partial HTML based on application data.
    """

    template_name = None

    @abstractmethod
    def get_context_data(self, **kwargs):
        ...

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return render(
            request,
            self.template_name,
            context
        )

class ActionView(ABC, View):
    """
    Base view for atomic state-changing operations.

    Executes a single mutation and returns a minimal response.
    """

    @abstractmethod
    def post(self, request, *args, **kwargs):
        ...