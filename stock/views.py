from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, ListView
from django.contrib import messages



# Admin part
from admin_login.models import zaptayAdmin

# Create your views here.

class ShowStockList(TemplateView):
    template_name = 'admin_template/inventory/stock_list.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ShowStockList, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('/site-admin/stock/')
            # return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        # seller_details = Seller.objects.all().order_by('-id')
        # context = {"page_name": "stock", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'seller': seller_details}
        context = {"page_name": "stock", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name}
        return context

class StockAddForm(TemplateView):
    template_name = 'admin_template/inventory/stock_entry_form.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(StockAddForm, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('/site-admin/stock/')
            # return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        # seller_details = Seller.objects.all().order_by('-id')
        # context = {"page_name": "stock", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'seller': seller_details}
        context = {"page_name": "stock", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name}
        return context
