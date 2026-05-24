from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View


class LoginActionView(View):

    def post(self, request):
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if not form.is_valid():
            return render(
                request,
                "users/partials/login_form.html",
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