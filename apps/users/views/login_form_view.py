from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from core.views import FormView


class LoginFormView(FormView):

    template_name = "users/login_form.html"
    form_class = AuthenticationForm
    success_url = "home"

    def form_valid(self, form):
        login(
            self.request,
            form.get_user()
        )

        response = HttpResponse(status=204)

        response["HX-Redirect"] = reverse(self.success_url)

        return response

    def form_invalid(self, form):
        return render(
            self.request,
            self.template_name,
            {
                "form": form
            },
            status=400
        )