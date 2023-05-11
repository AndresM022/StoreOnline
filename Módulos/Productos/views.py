from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class MainView(TemplateView):
    template_name = "navbar.html"

class FooterView(TemplateView):
    template_name = 'footer.html'