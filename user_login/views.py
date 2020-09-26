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

from home.base_template import BaseTemplateHeader

# Create your views here.


class LoginView(TemplateView):
    template_name = "user_template/login.html"

    def get_context_data(self, **kwargs):
        context = dict()

        obj = BaseTemplateHeader(self.request)
        base_template_data = obj.GetHeaderContent()

        context = {
            'base_template_content': base_template_data,
        }

        return context

class SignUpView(TemplateView):
    template_name = "user_template/signup.html"

    def get_context_data(self, **kwargs):
        context = dict()

        obj = BaseTemplateHeader(self.request)
        base_template_data = obj.GetHeaderContent()

        context = {
            'base_template_content': base_template_data,
        }

        return context



@csrf_exempt
def UserSignUp(request):
    '''
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
    '''

    if request.method == "POST" and request.is_ajax():
        name = request.POST['full_name']
        email_id = request.POST['email_id']
        phone_no = request.POST['phone_no']
        password = request.POST['passwd']

        if name == "" or email_id == "" or phone_no == "" or password == "":
            resp = {
                'status': 'Faield'
            }
        elif '' not in name:
            resp = {
                'status': 'Failed',
                'message': 'Name error'
            }
        else:
            try:
                create_user = UserAccount(user_f_name=name, email_id=email_id, ph_no=phone_no, passwd=password)
                create_user.save()
                print (create_user.user_custom_id)
                response = HttpResponse('user_login')
                resp = {
                    'status': 'Success'
                }
                response = JsonResponse(resp)
                response.set_cookie('login_user_id', create_user.user_custom_id, max_age=60) # 2592000
                return response
            except Exception as e:
                print (e)
    return JsonResponse(resp);

@csrf_exempt
def UserSignIn(request):
    # email = request.POST.get('email')
    # passwd = request.POST.get('passwd')

    email = request.POST.get('id')
    passwd = request.POST.get('pwd')

    create_user = UserAccount.objects.filter(email_id=email, passwd=passwd)
    if create_user.count() > 0:
        if not request.COOKIES.get('login_user_id'):
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
            response.set_cookie('login_user_id', user_id, max_age=60) # 2592000
        else:
            # print (request.COOKIES['user_id'] , 'cookie')
            data = {
                'status': 'Failed! Already login'
            }
            response = JsonResponse(data)
    else:
        data = {
            'status': 'Failed',
            'message': 'Invalid details'
        }
        response = JsonResponse(data)
    return response
