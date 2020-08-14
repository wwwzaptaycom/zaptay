from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from admin_login.models import zaptayAdmin
from .models import Banner

from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

class ViewBanner(TemplateView):
    template_name = 'admin_template/banner/all_banner_list.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ViewBanner, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/seller/seller-view/')
            return redirect('admin_login:admin_loginpage')

    def post(self, request, *args, **kwargs):
        try:
            if 'men_banner' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('men_banner')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "men-fashion-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/men_fashion/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/men_fashion/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='men_banner', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Men Banner Upload Successfull')

            if 'women_banner' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('women_banner')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "women-fashion-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/women_fashion/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/women_fashion/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='women_banner', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Women Banner Upload Successfull')

            if 'baby_kid_banner' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('baby_kid_banner')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "baby-kid-fashion-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/baby_kid_fashion/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/baby_kid_fashion/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='baby_kid_banner', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Baby & Kids Banner Upload Successfull')

            if 'mobile_banner' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('mobile_banner')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "mobile-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/mobile/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/mobile/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='mobile_banner', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Mobile Banner Upload Successfull')

            if 'electronics_banner' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('electronics_banner')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "electronic-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/electronic/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/electronic/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='electronic_banner', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Electronics Banner Upload Successfull')

            if 'office_appliance_banner' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('office_appliance_banner')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "office-appliance-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/officeappliance/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/officeappliance/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='office_appliance_banner', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Office Appliance Banner Upload Successfull')
        except Exception as e:
            print (e)

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = dict()
        seller_id = self.kwargs.get('seller_id')
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])

        get_mens_fashion = Banner.objects.filter(banner_name='men_banner').values('id', 'banner_image', 'banner_link')
        get_womens_fashion = Banner.objects.filter(banner_name='women_banner').values('id', 'banner_image', 'banner_link')
        get_baby_kid_fashion = Banner.objects.filter(banner_name='baby_kid_banner').values('id', 'banner_image', 'banner_link')
        get_mobile_fashion = Banner.objects.filter(banner_name='mobile_banner').values('id', 'banner_image', 'banner_link')
        get_electronic_fashion = Banner.objects.filter(banner_name='electronic_banner').values('id', 'banner_image', 'banner_link')
        get_office_appliance_fashion = Banner.objects.filter(banner_name='office_appliance_banner').values('id', 'banner_image', 'banner_link')

        context = {"page_name": "banner", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name,
                    'men_fashion_image': get_mens_fashion,
                    'women_fashion_image': get_womens_fashion,
                    'baby_kid_fashion_image': get_baby_kid_fashion,
                    'mobile_image': get_mobile_fashion,
                    'electronic_image': get_electronic_fashion,
                    'office_appliance_image': get_office_appliance_fashion}
        return context
