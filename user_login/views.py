from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import View, TemplateView, FormView, ListView
from django.contrib import messages

from user_login.models import UserAccount

from django.views.decorators.csrf import csrf_exempt

# =================================================================

from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView

from django.db.models import Subquery

from banner.models import Banner
from category.models import MainCategory
from attribute.models import SubCategory, TertiaryCategory
from product.models import Product, ProductImage
from stock.models import Bach, Inventory
from offer.models import Offer, OfferProduct
from user_login.models import UserAccount

from django.utils import timezone
from datetime import datetime

# Create your views here.


class LoginView(TemplateView):
    template_name = "user_template/login.html"

    def get_context_data(self, **kwargs):
        context = dict()

        header_logo = get_header_logo = Banner.objects.filter(banner_name='header_logo').order_by('-id').first()

        megamenu = list()
        featured_category = MainCategory.objects.filter(main_category_name='featured').first()
        get_sub_category = SubCategory.objects.filter(category_id=featured_category)
        for i in get_sub_category:
            sub_category = list()
            sub_category.append(i.sub_category_name)
            get_tertiary_category = TertiaryCategory.objects.filter(sub_category_id=i)
            tertiary_cate_ar = list()
            for j in get_tertiary_category:
                tertiary_cate = dict()
                tertiary_cate['id'] = j.ter_category_id
                tertiary_cate['name'] = j.ter_category_name
                tertiary_cate_ar.append(tertiary_cate)
            sub_category.append(tertiary_cate_ar)
            megamenu.append(sub_category)
        # print (megamenu)

        featured_category = MainCategory.objects.filter(main_category_name='exclusive').first()
        get_more_sub_category = SubCategory.objects.filter(category_id=featured_category)
        # print (featured_category)

        context = {
            'header_logo': header_logo,
            'mega_menu_sub_category': megamenu,
            'mega_menu_more_category': get_more_sub_category,
        }

        return context

class SignUpView(TemplateView):
    template_name = "user_template/signup.html"

    def get_context_data(self, **kwargs):
        context = dict()

        header_logo = get_header_logo = Banner.objects.filter(banner_name='header_logo').order_by('-id').first()

        megamenu = list()
        featured_category = MainCategory.objects.filter(main_category_name='featured').first()
        get_sub_category = SubCategory.objects.filter(category_id=featured_category)
        for i in get_sub_category:
            sub_category = list()
            sub_category.append(i.sub_category_name)
            get_tertiary_category = TertiaryCategory.objects.filter(sub_category_id=i)
            tertiary_cate_ar = list()
            for j in get_tertiary_category:
                tertiary_cate = dict()
                tertiary_cate['id'] = j.ter_category_id
                tertiary_cate['name'] = j.ter_category_name
                tertiary_cate_ar.append(tertiary_cate)
            sub_category.append(tertiary_cate_ar)
            megamenu.append(sub_category)
        # print (megamenu)

        featured_category = MainCategory.objects.filter(main_category_name='exclusive').first()
        get_more_sub_category = SubCategory.objects.filter(category_id=featured_category)
        # print (featured_category)

        context = {
            'header_logo': header_logo,
            'mega_menu_sub_category': megamenu,
            'mega_menu_more_category': get_more_sub_category,
        }

        return context



@csrf_exempt
def UserSignUp(request):
    f_name = request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    gender = request.POST.getlist('gender')
    email = request.POST.get('email')
    passwd = request.POST.get('passwd')

    create_user = UserAccount(user_f_name=f_name, user_l_name=l_name, gender=gender[0], email_id=email, passwd=passwd)
    create_user.save()
    print (request.COOKIES.get('user_id'))

    data = {
        'status': 'Success'
    }
    return JsonResponse(data)

@csrf_exempt
def UserSignIn(request):
    email = request.POST.get('email')
    passwd = request.POST.get('passwd')

    create_user = UserAccount.objects.filter(email_id=email, passwd=passwd)
    if create_user.count() > 0:
        if not request.COOKIES.get('user_id'):
            response = HttpResponse('user_login')
            user_id = create_user[0].user_custom_id
            '''
            max_age = 14*24*60*60 # two weeks
            expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
            response.set_cookie('user_id', user_id, max_age=max_age, expires=expires) # 2592000
            print (request.COOKIES , 'cookie')
            '''
            data = {
                'status': 'Success'
            }
            response = JsonResponse(data)
            response.set_cookie('user_id', user_id, max_age=2592000) # 2592000
        else:
            print (request.COOKIES['user_id'] , 'cookie')
            data = {
                'status': 'Failed! Already login'
            }
            response = JsonResponse(data)
    return response
