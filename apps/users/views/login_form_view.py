from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from core.views import FormView


class LoginFormView(FormView):

    template_name = "users/login_form.html"
    form_class = AuthenticationForm
    success_url = "home"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)