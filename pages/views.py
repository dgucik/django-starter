from time import time

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from core.mixins import HtmxFormMixin


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['positions'] = POSITIONS
        return ctx

class AboutPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/about.html'

class LoginPageView(TemplateView):
    template_name = "pages/login.html"

class TriggerDelayView(TemplateView):
    template_name = "pages/trigger_delay.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        q = self.request.GET.get("q", "")
        data = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"},

        ]
        ctx["results"] = [d for d in data if q.lower() in d["name"].lower()]
        ctx["query"] = q
        return ctx
    

class PositionForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    product = forms.CharField(max_length=100)
    quantity = forms.IntegerField(min_value=1)
    price = forms.DecimalField(max_digits=10, decimal_places=2)

POSITIONS = [
    {"id": 1, "product": "Widget A", "quantity": 3, "price": "19.99"},
    {"id": 2, "product": "Widget B", "quantity": 1, "price": "49.00"},
]


class PositionsPartialView(View):
    def get(self, request):
        forms = [PositionForm(initial=p) for p in POSITIONS]
        return render(request, "pages/partials/positions_tbody.html", {"forms": forms})


class PositionView(View):
    def get(self, request):
        return render(request, "pages/partials/positions_row_form.html", {"form": PositionForm()})

    def post(self, request):
        print(request.POST)

        ids = request.POST.getlist("id")
        products = request.POST.getlist("product")
        quantities = request.POST.getlist("quantity")
        prices = request.POST.getlist("price")

        for _id, product, quantity, price in zip(ids, products, quantities, prices):
            print(_id, product, quantity, price)
            if _id:
                continue  # Skip existing positions for this example
            _id = int(time())  # Generate a new ID based on the current timestamp
            form = PositionForm({"id": _id, "product": product, "quantity": quantity, "price": price})
            if form.is_valid():
                POSITIONS.append(form.cleaned_data)

        response = HttpResponse(status=204)
        response["HX-Trigger"] = "positionsSaved"
        return response


