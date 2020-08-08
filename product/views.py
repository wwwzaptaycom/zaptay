from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, ListView
from django.contrib import messages

from .product_form import ProductForm
from .models import Product
from category.models import MainCategory
from attribute.models import SubCategory, TertiaryCategory, Colour, Size, Source, SameDayDelivary, NextDayDelivary
from seller.models import Seller

# Admin part
from admin_login.models import zaptayAdmin

# Create your views here.

'''
class ShowProductList(ListView):
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views   (help)
    template_name = 'admin_template/product_list.html'
'''
class ShowProductList(TemplateView):
    template_name = 'admin_template/product_list.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ShowProductList, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        product_list = Product.objects.all().order_by('-id')
        context = {"page_name": "product_list", "admin_name": get_name.admin_f_name+" "+get_name.admin_l_name, 'product_list': product_list}
        return context

class ShowProductForm(FormView):
    form_class = ProductForm
    template_name = 'admin_template/product_form.html'
    success_url = '/site-admin/product/product-form'

    '''
    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ShowProductForm, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/product/product-form')
            return redirect('admin_login:admin_loginpage')
    '''

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "add_product", "admin_name": get_name.admin_f_name+" "+get_name.admin_l_name, 'form': self.form_class}
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            product_title = request.POST['product_title']
            '''
            main_price = request.POST['main_price']
            offer_price = request.POST['offer_price']
            extra_price = request.POST['extra_price']
            purchase_price = request.POST['purchase_price']
            '''
            category = request.POST['category']
            sub_category = request.POST['sub_cateegory']
            tertiary_category = request.POST['tertiary']
            seller = request.POST['seller']
            prod_desc = request.POST['description']
            color = request.POST['color']
            size = request.POST['size']
            source = request.POST['made_in']
            youtube = request.POST['youtube']

            # same_day_delivary=same_day_delivary_price=next_day_delivary=next_day_delivary_price=customize_day_delivary=customize_day_delivary_price=customize_day_delivary_day=0

            same_day_delivary=next_day_delivary=customize_day_delivary=weekly_dreals=top_offer=return_product=cod=False
            same_day_delivary_price=next_day_delivary_price=customize_day_delivary_price=customize_day_delivary_day=0

            if 'same_day_delivary_check' in request.POST:
                # same_day_delivary = request.POST['same_day_delivary_check']
                same_day_delivary = True
                same_day_delivary_price = request.POST['same_day_delivary_price']
            if 'next_day_delivary_check' in request.POST:
                # next_day_delivary = request.POST['next_day_delivary_check']
                next_day_delivary = True
                next_day_delivary_price = request.POST['next_day_delivary_price']
            if 'customize_delivary_check' in request.POST:
                # customize_day_delivary = request.POST['customize_delivary_check']
                customize_day_delivary = True
                customize_day_delivary_price = request.POST['customize_delivary_price']
                customize_day_delivary_day = request.POST['customize_delivary_day']

            weekly_dreals=top_offer=free_shiping=return_product=cod =0
            if 'weekly_dreals' in request.POST:
                # weekly_dreals = request.POST['weekly_dreals']
                weekly_dreals = True
            if 'top_offer' in request.POST:
                # top_offer = request.POST['top_offer']
                top_offer = True
            '''
            if 'free_shiping' in request.POST:
                free_shiping = request.POST['free_shiping']
            '''
            if 'return_product' in request.POST:
                # return_product = request.POST['return_product']
                return_product = True
            if 'cod' in request.POST:
                # cod = request.POST['cod']
                cod = True

            '''
            print ("*********************************************************************************")
            print (product_title,main_price,offer_price,extra_price,purchase_price,category,sub_category,tertiary_category,prod_desc,color,size,source,youtube,
            weekly_dreals,top_offer,free_shiping,return_product,cod,same_day_delivary,same_day_delivary_price,next_day_delivary,next_day_delivary_price,
            customize_day_delivary,customize_day_delivary_price,customize_day_delivary_day)
            '''

            get_category_id_object = MainCategory.objects.all().filter(category_id=category).first()
            sub_category_id_object = SubCategory.objects.all().filter(sub_category_id=sub_category).first()
            tertiary_category_id_object = TertiaryCategory.objects.all().filter(ter_category_id=tertiary_category).first()
            color_id_object = Colour.objects.all().filter(color_id=color).first()
            size_id_object = Size.objects.all().filter(size_id=size).first()
            source_id_object = Source.objects.all().filter(source_id=source).first()
            seller_id_object = Seller.objects.all().filter(seller_id=seller).first()
            admin_id = zaptayAdmin.objects.all().filter(email_id=request.session.get('admin_email_id')).first()

            store_product = Product(
                            prod_title=product_title,
                            prod_category=get_category_id_object,
                            prod_sub_category=sub_category_id_object,
                            prod_tertiary_category=tertiary_category_id_object,
                            prod_color=color_id_object,
                            prod_size=size_id_object,
                            prod_made_in=source_id_object,
                            seller=seller_id_object,
                            prod_desc=prod_desc,
                            same_day_delivery=same_day_delivary,
                            same_day_delivery_price=same_day_delivary_price,
                            next_day_delivery=next_day_delivary,
                            next_day_delivery_price=next_day_delivary_price,
                            customize_day_delivery=customize_day_delivary,
                            customize_day_delivery_day=customize_day_delivary_day,
                            customize_day_delivery_price=customize_day_delivary_price,
                            weekly_dreals=weekly_dreals,
                            top_offer=top_offer,
                            product_return=return_product,
                            cash_on_delivery=cod,
                            youtube_link=youtube,
                            added_by=admin_id)
            store_product.save()
            messages.success(request, 'Product inserted successfull')

            # return self.form_valid(form) # 100% correct tested
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        # context = self.get_context_data(task_form=form)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
        '''
        if 'weekly_dreals' in request.POST and request.POST['weekly_dreals'] == 'on':
            print(request.POST['weekly_dreals'])
        # print (request.FILES)
        context = {"db_error": "Authentication failure",'form':form}
        return self.render_to_response(context)
        '''
