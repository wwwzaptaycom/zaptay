from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView

from banner.models import Banner

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = dict()
        get_mens_fashion = Banner.objects.filter(banner_name='men_banner').values('id', 'banner_image', 'banner_link')
        # print (get_mens_fashion)
        get_womens_fashion = Banner.objects.filter(banner_name='women_banner').values('id', 'banner_image', 'banner_link')
        context = {"page_name": "banner", 'mens_banner_image': get_mens_fashion, 'womens_banner_image': get_womens_fashion}
        return context
