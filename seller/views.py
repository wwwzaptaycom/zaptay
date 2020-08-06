from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView

from admin_login.models import zaptayAdmin

# Create your views here.

class AddSellerForm(TemplateView):
    template_name = 'admin_template/seller/seller_form.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(AddSellerForm, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "add_seller", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name}
        return context
