from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from admin_login.models import zaptayAdmin

from .seller_form import SellerForm
from .models import Seller

# Create your views here.

class ViewSellerList(ListView):
    template_name = 'admin_template/seller/seller_list.html'
    model = Seller

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ViewSellerList, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('/site-admin/seller/all-seller/')
            # return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        seller_details = Seller.objects.all().order_by('-id')
        context = {"page_name": "add_seller", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'seller': seller_details}
        return context

class ViewSeller(TemplateView):
    template_name = 'admin_template/seller/seller.html'
    model = Seller

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ViewSeller, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/seller/seller-view/')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        seller_id = self.kwargs.get('seller_id')
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        seller_details = Seller.objects.all().filter(seller_id=seller_id).first()
        context = {"page_name": "add_seller", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'seller': seller_details}
        return context

class EditSeller(FormView):
    form_class = SellerForm
    template_name = 'admin_template/seller/seller_form.html'
    success_url = '/site-admin/seller/all-seller/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(EditSeller, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/seller/add-seller/')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        seller_id = self.kwargs.get('seller_id')
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        seller_details = Seller.objects.all().filter(seller_id__icontains=seller_id).first()
        edit_form = SellerForm(initial={
            'seller_title': seller_details.seller_title,
            'seller_name': seller_details.seller_name,
            'seller_email': seller_details.seller_email_id,
            'seller_phone_no': seller_details.seller_phone_no,
            'seller_gst_no': seller_details.seller_gst_no,
            'seller_aadhaar_no': seller_details.seller_aadhaar_no,
            'seller_voter_no': seller_details.seller_voter_no
        })
        context = {"page_name": "add_seller", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'form':edit_form, 'seller_data':seller_details}
        return context

class AddSellerForm(FormView):
    form_class = SellerForm
    template_name = 'admin_template/seller/seller_form.html'
    success_url = '/site-admin/seller/add-seller/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(AddSellerForm, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('/site-admin/seller/add-seller/')
            # return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "add_seller", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, 'form':self.form_class}
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            seller_title = request.POST['seller_title']
            seller_name = request.POST['seller_name']
            seller_email = request.POST['seller_email']
            seller_phone_no = request.POST['seller_phone_no']
            seller_gst_no = request.POST['seller_gst_no']
            seller_aadhaar_no = request.POST['seller_aadhaar_no']
            seller_voter_no = request.POST['seller_voter_no']

            # Image document
            seller_img=gst_img=aadhaar_img=voter_img=''
            if 'seller_img' in request.FILES:
                seller_img = request.FILES['seller_img']
            if 'gst_img' in request.FILES:
                gst_img = request.FILES['gst_img']
            if 'aadhaar_img' in request.FILES:
                aadhaar_img = request.FILES.getlist('aadhaar_img')
            if 'voter_img' in request.FILES:
                voter_img = request.FILES.getlist('voter_img')

            '''
            print ("**********************Image*******************************")
            print (seller_img,gst_img,aadhaar_img,voter_img)
            print (aadhaar_img[0].content_type)
            '''

            admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))
            seller_data = Seller(seller_title=seller_title,seller_name=seller_name,seller_email_id=seller_email,seller_phone_no=seller_phone_no,seller_gst_no=seller_gst_no,seller_aadhaar_no=seller_aadhaar_no,seller_voter_no=seller_voter_no, added_by=admin_id)
            print (seller_data)
            seller_data.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        # context = self.get_context_data(task_form=form)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


# ******************************************************************************************************************
# Ajax hendel

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

@csrf_exempt
def SearchSeller(request):
    all_fields_list = list()
    search_key = request.GET.get('search_keyword')
    get_data = Seller.objects.all().filter(seller_id__icontains=search_key)
    for shop_data in get_data:
        all_fields = dict()
        all_fields['seller_id'] = shop_data.seller_id
        all_fields['seller_title'] = shop_data.seller_title
        all_fields['seller_email_id'] = shop_data.seller_email_id
        all_fields['seller_phone_no'] = shop_data.seller_phone_no
        all_fields['id'] = shop_data.id
        all_fields['active'] = shop_data.is_active

        all_fields_list.append(all_fields)

    if request.is_ajax() and request.method == "GET":
        data = {
	        'status': 'success',
            "resp": all_fields_list
	    }
    else:
        data = {
	        'status': 'error'
	    }

    return JsonResponse(data)
    # return HttpResponse(message)
