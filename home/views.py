from django.shortcuts import render

from django.views.generic import View, TemplateView, FormView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
