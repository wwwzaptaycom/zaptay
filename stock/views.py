from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, ListView
from django.contrib import messages

from .stock_form import StockEntryForm
from django.db.models import Q
from product.models import Product, ProductImage
from .models import Bach, Inventory

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
        stock_details = Bach.objects.all().order_by("-id")
        # print (stock_details)
        context = {"page_name": "stock", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'stock_list': stock_details}
        return context

class StockAddForm(FormView):
    form_class = StockEntryForm
    template_name = 'admin_template/inventory/stock_entry_form.html'
    success_url = '/site-admin/stock/'

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
        context = {"page_name": "stock", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'form': self.form_class}
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            product_id = request.POST['product_id']
            stock = request.POST['stock']
            main_price = request.POST['main_price']
            offer_price = request.POST['offer_price']
            # extra_offer = request.POST['extra_offer']
            purchase = request.POST['purchase']
            # print (product_id,stock,main_price,offer_price,purchase)
            product_id_db = Product.objects.all().filter(prod_custom_id=product_id).first()
            admin_id = zaptayAdmin.objects.all().filter(email_id=request.session.get('admin_email_id')).first()

            bach_entry = Bach(product_id=product_id_db, stock=stock, main_price=main_price, offer_price=offer_price, purchase_price=purchase, added_by=admin_id)
            bach_entry.save()

            # *******************************************************************************
            # Inventory Update
            # *******************************************************************************
            # print (bach_entry.id, bach_entry.bach_id)
            store_inventory = Inventory(bach_id=bach_entry, product_id=product_id_db, qty=stock, remaining_stock=stock, inventory_status="stock_in", added_by=admin_id)
            store_inventory.save()

            messages.success(request, "Stock add successful")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        # context = self.get_context_data(task_form=form)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

class StockViewForm(TemplateView):
    template_name = 'admin_template/inventory/stock_entry_view.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(StockViewForm, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('/site-admin/stock/')
            # return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        product_id = self.kwargs.get('product_id')
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])

        stock_details = Bach.objects.filter(bach_id=product_id).first()
        print (stock_details)
        context = {"page_name": "stock", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'stock_details': stock_details}
        return context

# AJAX Functions
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

@csrf_exempt
def SearchProduct(request):
    search_key = request.GET.get('search_keyword')
    search_by = request.GET.get('search_by')
    if search_by == "product_id":
        product_list_data = Product.objects.filter(prod_custom_id__icontains=search_key)
    if search_by == "product_name":
        product_list_data = Product.objects.filter(prod_title__icontains=search_key)

    product_list = list()
    for product in product_list_data:
        product_dict = dict()
        product_dict['product_id'] = product.id
        product_dict['product_custom_id'] = product.prod_custom_id
        product_dict['product_title'] = product.prod_title
        product_dict['product_category'] = product.prod_category.main_category_name
        product_dict['product_sub_category'] = product.prod_sub_category.sub_category_name
        product_dict['product_seller'] = product.seller.seller_name
        if product.prod_tertiary_category != None:
            product_dict['product_tertiary_category'] = product.prod_tertiary_category.ter_category_name

        product_list.append(product_dict)
    data = {
        'resp': product_list,
        'status': 'error'
    }
    return JsonResponse(data)

@csrf_exempt
def ViewProduct(request):
    product_id = request.GET.get('product_id')
    product_list = list()
    product_list_data = Product.objects.filter(prod_custom_id__icontains=product_id)
    for product in product_list_data:
        product_dict = dict()
        product_dict['product_id'] = product.id
        product_dict['product_custom_id'] = product.prod_custom_id
        product_dict['product_title'] = product.prod_title
        product_dict['product_category'] = product.prod_category.main_category_name
        product_dict['product_sub_category'] = product.prod_sub_category.sub_category_name
        product_dict['product_seller'] = product.seller.seller_name
        if product.prod_tertiary_category != None:
            product_dict['product_tertiary_category'] = product.prod_tertiary_category.ter_category_name
        if product.prod_color != None:
            product_dict['product_color'] = product.prod_color.color_name
        if product.prod_size != None:
            product_dict['product_size'] = product.prod_size.size_name
        product_dict['product_made_in'] = product.prod_made_in.source_name

        product_list.append(product_dict)
    data = {
        'resp': product_list,
        'status': 'error'
    }
    return JsonResponse(data)
