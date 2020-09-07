from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import View, TemplateView, FormView, ListView
from django.contrib import messages

from user_login.models import UserAccount

from django.views.decorators.csrf import csrf_exempt

'''
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
import datetime
import time
'''

# Create your views here.

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
