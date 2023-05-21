from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class MainView(TemplateView):
    template_name = "main.html"

class CamisetaView(TemplateView):
    template_name = "camisetas.html"
