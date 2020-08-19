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
        get_baby_kid_fashion = Banner.objects.filter(banner_name='baby_kid_banner').values('id', 'banner_image', 'banner_link')
        get_mobile_fashion = Banner.objects.filter(banner_name='mobile_banner').values('id', 'banner_image', 'banner_link')
        get_electronic_fashion = Banner.objects.filter(banner_name='electronic_banner').values('id', 'banner_image', 'banner_link')
        get_office_fashion = Banner.objects.filter(banner_name='office_appliance_banner').values('id', 'banner_image', 'banner_link')

        banner_1 = Banner.objects.filter(banner_name='advatice_1').order_by('-id')[0:3]
        banner_2 = Banner.objects.filter(banner_name='advatice_2').order_by('-id')[0:2]

        context = {"page_name": "banner",
                    'mens_banner_image': get_mens_fashion,
                    'womens_banner_image': get_womens_fashion,
                    'baby_kid_banner_image': get_baby_kid_fashion,
                    'mobile_banner_image': get_mobile_fashion,
                    'electronic_banner_image': get_electronic_fashion,
                    'electronic_office_image': get_office_fashion,
                    'banner_1': banner_1,
                    'banner_2': banner_2}
        return context
