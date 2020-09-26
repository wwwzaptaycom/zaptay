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
                return redirect('/site-admin/banner/')

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
                return redirect('/site-admin/banner/')

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
                return redirect('/site-admin/banner/')

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
                return redirect('/site-admin/banner/')

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
                return redirect('/site-admin/banner/')

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
                return redirect('/site-admin/banner/')

            if 'advatice_1' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_1')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-1-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice1/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice1/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='advatice_1', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 1 Upload Successfull')
                return redirect('/site-admin/banner/')

            if 'advatice_2' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_2')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-2-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice2/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice2/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='advatice_2', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 2 Upload Successfull')
                return redirect('/site-admin/banner/')

            if 'advatice_3' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_3')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-3-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice3/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice3/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='advatice_3', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 3 Upload Successfull')
                return redirect('/site-admin/banner/')

            if 'advatice_4' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_4')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-4-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice4/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice4/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='advatice_4', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 4 Upload Successfull')
                return redirect('/site-admin/banner/')

            if 'advatice_5' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_5')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-5-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice5/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice5/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='advatice_5', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 5 Upload Successfull')
                return redirect('/site-admin/banner/')

            if 'advatice_6' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_6')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-6-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice6/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice6/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='advatice_6', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner 6 Upload Successfull')
                return redirect('/site-admin/banner/')

            if 'advatice_right' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_right')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-right-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice_right/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice_right/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='advatice_right', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner Right Upload Successfull')
                return redirect('/site-admin/banner/')

            if 'advatice_left' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('advatice_left')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "advatice-right-banner."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/advatice_left/images/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/advatice_left/images/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='advatice_left', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Advatice Banner Left Upload Successfull')
                return redirect('/site-admin/banner/')

            # *******************************   Banner title    ***********************************************
            # print (request.POST)
            # return
            if 'men_banner_title' in request.POST:
                banner_custom_title = request.POST.getlist('men_banner_title')
                if banner_custom_title[0] != "":
                    edit_banner_custom_title = Banner.objects.filter(banner_name='men_banner').update(banner_name_custom=banner_custom_title[0])
            if 'women_banner_title' in request.POST:
                banner_custom_title = request.POST.getlist('women_banner_title')
                if banner_custom_title[0] != "":
                    edit_banner_custom_title = Banner.objects.filter(banner_name='women_banner').update(banner_name_custom=banner_custom_title[0])
            if 'baby_kid_banner_title' in request.POST:
                banner_custom_title = request.POST.getlist('baby_kid_banner_title')
                if banner_custom_title[0] != "":
                    edit_banner_custom_title = Banner.objects.filter(banner_name='baby_kid_banner').update(banner_name_custom=banner_custom_title[0])
            if 'mobile_banner_title' in request.POST:
                banner_custom_title = request.POST.getlist('mobile_banner_title')
                if banner_custom_title[0] != "":
                    edit_banner_custom_title = Banner.objects.filter(banner_name='mobile_banner').update(banner_name_custom=banner_custom_title[0])

            if 'electronic_banner_title' in request.POST:
                banner_custom_title = request.POST.getlist('electronic_banner_title')
                if banner_custom_title[0] != "":
                    edit_banner_custom_title = Banner.objects.filter(banner_name='electronic_banner').update(banner_name_custom=banner_custom_title[0])

            if 'office_appliance_banner_title' in request.POST:
                banner_custom_title = request.POST.getlist('office_appliance_banner_title')
                if banner_custom_title[0] != "":
                    edit_banner_custom_title = Banner.objects.filter(banner_name='office_appliance_banner').update(banner_name_custom=banner_custom_title[0])

            # *******************************   Banner title    ***********************************************
        except Exception as e:
            print (e)

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = dict()
        seller_id = self.kwargs.get('seller_id')
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])

        get_mens_fashion = Banner.objects.filter(banner_name='men_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')
        get_womens_fashion = Banner.objects.filter(banner_name='women_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')
        get_baby_kid_fashion = Banner.objects.filter(banner_name='baby_kid_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')
        get_mobile_fashion = Banner.objects.filter(banner_name='mobile_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')
        get_electronic_fashion = Banner.objects.filter(banner_name='electronic_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')
        get_office_appliance_fashion = Banner.objects.filter(banner_name='office_appliance_banner').values('id', 'banner_image', 'banner_link', 'banner_id', 'banner_name_custom')

        get_advatice_banner_1 = Banner.objects.filter(banner_name='advatice_1').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_2 = Banner.objects.filter(banner_name='advatice_2').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_3 = Banner.objects.filter(banner_name='advatice_3').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_4 = Banner.objects.filter(banner_name='advatice_4').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_5 = Banner.objects.filter(banner_name='advatice_5').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_6 = Banner.objects.filter(banner_name='advatice_6').values('id', 'banner_image', 'banner_link', 'banner_id')

        get_advatice_banner_right = Banner.objects.filter(banner_name='advatice_right').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_advatice_banner_left = Banner.objects.filter(banner_name='advatice_left').values('id', 'banner_image', 'banner_link', 'banner_id')

        context = {"page_name": "banner", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name,
                    'men_fashion_image': get_mens_fashion,
                    'women_fashion_image': get_womens_fashion,
                    'baby_kid_fashion_image': get_baby_kid_fashion,
                    'mobile_image': get_mobile_fashion,
                    'electronic_image': get_electronic_fashion,
                    'office_appliance_image': get_office_appliance_fashion,
                    'advatice_banner_1_image': get_advatice_banner_1,
                    'advatice_banner_2_image': get_advatice_banner_2,
                    'advatice_banner_3_image': get_advatice_banner_3,
                    'advatice_banner_4_image': get_advatice_banner_4,
                    'advatice_banner_5_image': get_advatice_banner_5,
                    'advatice_banner_6_image': get_advatice_banner_6,
                    'advatice_banner_right_image': get_advatice_banner_right,
                    'advatice_banner_left_image': get_advatice_banner_left}
        return context

class WebSiteLogo(TemplateView):
    template_name = 'admin_template/website_logo/website_logo.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(WebSiteLogo, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/seller/seller-view/')
            return redirect('admin_login:admin_loginpage')

    def post(self, request, *args, **kwargs):
        try:
            if 'header_logo' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('header_logo')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "website_header_logo."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/website/header_logo/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/website/header_logo/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='header_logo', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Website header logo Upload Successfull')
                return redirect('/site-admin/banner/website-logo/')

            if 'footer_logo' in request.FILES:
                banner_link = request.POST.getlist('banner_link')
                men_banner_image = request.FILES.getlist('footer_logo')
                for image, link in zip(men_banner_image, banner_link):
                    # print (image)
                    # print (link)
                    fs = FileSystemStorage()
                    image_title = "website_footer_logo."+image.name.split(".")[-1]
                    upload_image = fs.save("banner/website/footer_logo/"+image_title, image)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'banner/website/footer_logo/'+mod_image_name

                    image_upload = Banner(banner_image=image_path, banner_name='footer_logo', banner_link=link)
                    image_upload.save()
                messages.success(request, 'Website footer logo Upload Successfull')
                return redirect('/site-admin/banner/website-logo/')
        except Exception as e:
            print (e)

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = dict()
        seller_id = self.kwargs.get('seller_id')
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])

        get_header_logo = Banner.objects.filter(banner_name='header_logo').values('id', 'banner_image', 'banner_link', 'banner_id')
        get_footer_logo = Banner.objects.filter(banner_name='footer_logo').values('id', 'banner_image', 'banner_link', 'banner_id')

        context = {"page_name": "logo",
                    "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name,
                    "get_header_logo": get_header_logo,
                    "get_footer_logo": get_footer_logo,
                }
        return context

# ******************************************************************************************************************
# Ajax hendel

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import os

@csrf_exempt
def DeleteBannerImage(request):
    image_id = request.POST['image_id']

    del_img = Banner.objects.get(pk=image_id)
    del_img.delete()
    # del_image_path = Banner.objects.get(pk=image_id)
    # print (del_image_path.banner_image)
    os.remove('media/'+str(del_img.banner_image))

    data = {
        'status': 'success',
    }
    return JsonResponse(data)
