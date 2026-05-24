from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views import View


class LoginFormPartialView(View):

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
    
