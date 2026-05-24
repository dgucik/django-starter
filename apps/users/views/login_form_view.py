from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View


class LoginFormView(View):

    template_name = "users/login_form.html"

    def get(self, request):
        form = AuthenticationForm()

        return render(
            request,
            self.template_name,
            {
                "form": form
            }
        )

    def post(self, request):
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    "form": form
                },
                status=400
            )

        login(
            request,
            form.get_user()
        )

        response = HttpResponse(status=204)

        response["HX-Redirect"] = reverse("home")

        return response