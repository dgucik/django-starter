from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.urls import reverse
from core.mixins import HtmxRequiredMixin
from django.views import View
from django.shortcuts import render

class LoginFormView(HtmxRequiredMixin, View):

    template_name = "users/login_form.html"
    form_class = AuthenticationForm
    success_url = "home"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        
        login(request, form.get_user())
        response = HttpResponse(status=204)
        response["HX-Redirect"] = reverse(self.success_url)
        return response