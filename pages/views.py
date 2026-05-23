from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/about.html'

class LoginPageView(LoginView):
    template_name = "pages/login.html"
    redirect_authenticated_user = True