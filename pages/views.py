from django.contrib.auth.mixins import LoginRequiredMixin

from core.views import PageView

class HomePageView(LoginRequiredMixin, PageView):
    template_name = 'pages/home.html'

class AboutPageView(LoginRequiredMixin, PageView):
    template_name = 'pages/about.html'

class LoginPageView(PageView):
    template_name = "pages/login.html"