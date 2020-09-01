from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, ListView
from django.contrib import messages

from django.db.models import Q, Subquery
from . models import Offer, OfferProduct
from product.models import Product
from stock.models import Bach

from admin_login.models import zaptayAdmin

# Create your views here.

# Admin views =============================================================================
class ShowOfferList(TemplateView):
    template_name = 'admin_template/offer/offer_list.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ShowOfferList, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/stock/')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        get_offer_list = Offer.objects.all().order_by('-id')
        context = {"page_name": "offer", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'offers': get_offer_list}
        return context

class ShowOfferForm(TemplateView):
    template_name = 'admin_template/offer/offer_form.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ShowOfferForm, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('/site-admin/offer/create-offer')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        # print (stock_details)
        context = {"page_name": "offer", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name}
        return context

    def post(self, request, *args, **kwargs):
        try:
            offer_title = request.POST['offer_title']
            offer_start = request.POST['start_date_time'].replace("T", " ")
            offer_end = request.POST['end_date_time'].replace("T", " ")

            admin_id = zaptayAdmin.objects.all().filter(email_id=request.session.get('admin_email_id')).first()
            offer_add = Offer(offer_title=offer_title, offer_start=offer_start, offer_end=offer_end, added_by = admin_id)
            offer_add.save()

            '''
            context = self.get_context_data()
            return self.render_to_response(context)
            '''
            return redirect('admin_login:offer:edit_offer', offer_id=offer_add.offer_custom_id)
        except Exception as e:
            print(e)
            return redirect('/site-admin/offer/create-offer')
            # return redirect('admin_login:admin_loginpage')

class EditOfferForm(TemplateView):
    template_name = 'admin_template/offer/offer_form_edit.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(EditOfferForm, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('/site-admin/offer/edit-offer')
            # return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        offer_id = self.kwargs.get('offer_id')
        get_offer_detils = Offer.objects.all().get(offer_custom_id=offer_id)
        # print (get_offer_detils.offer_start)
        start_date = str(get_offer_detils.offer_start).replace(" ", "T")
        start_date = start_date.replace("+00:00", "")
        end_date = str(get_offer_detils.offer_end).replace(" ", "T")
        end_date = end_date.replace("+00:00", "")
        context = {"page_name": "offer", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'offer_details': get_offer_detils, 'start_time': start_date, 'end_time': end_date}
        return context


# Ajax methos

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

@csrf_exempt
def SearchProductBatch(request):
    product_id = request.GET.get('product_id')
    product_list = Product.objects.filter(prod_custom_id=product_id)
    bach_list = Bach.objects.filter(product_id=product_list.first())
    print(product_list)
    print (bach_list)

    product = [product_list[0].prod_custom_id, product_list[0].prod_title]
    print (type(product), product)

    bach = list()
    for i in bach_list:
        bach_dict = dict()
        bach_dict['bach_id'] = i.bach_id
        bach_dict['stock'] = i.stock
        bach_dict['entry'] = str(i.create_date)
        bach.append(bach_dict)
    print (bach)

    data = {
        'status': 'success',
        'product':product,
        'stock': bach
    }
    return JsonResponse(data)

@csrf_exempt
def InsertOfferProduct(request):
    product_id = Product.objects.filter(prod_custom_id=request.POST['product_id']).first()
    offer_id = Offer.objects.filter(offer_custom_id=request.POST['offer_id']).first()

    admin_id = zaptayAdmin.objects.all().filter(email_id=request.session.get('admin_email_id')).first()
    insert_product = OfferProduct(offer_id = offer_id, product_id = product_id, extra_offer_price = request.POST['offer_price'], added_by=admin_id)
    insert_product.save()

    data = {
        'status': 'success',

    }
    return JsonResponse(data)

@csrf_exempt
def OfferProductLisr(request):
    product_list = OfferProduct.objects.filter(offer_id__in=Subquery(Offer.objects.filter(offer_custom_id=request.POST['offer_id']).values('id')))
    # print (product_list)
    product_data = list()
    for product in product_list:
        product_dict = dict()
        product_dict['offer_pro_id'] = product.id
        product_dict['product_id'] = product.product_id.prod_custom_id
        product_dict['product_name'] = product.product_id.prod_title

        product_data.append(product_dict)

    print (product_data)
    data = {
        'status': 'success',
        'data': product_data
    }
    return JsonResponse(data)
