from django.shortcuts import render

from django.views.generic import View, TemplateView, FormView

# Create your views here.

class CategoryViews(TemplateView):
    template_name = 'category.html'
