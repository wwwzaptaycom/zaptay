from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from admin_login.models import zaptayAdmin

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

    def get_context_data(self, **kwargs):
        context = dict()
        seller_id = self.kwargs.get('seller_id')
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "banner", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name}
        return context
