from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, ListView
from django.contrib import messages

from .product_form import ProductForm
from .models import Product, ProductImage
from category.models import MainCategory
from attribute.models import SubCategory, TertiaryCategory, Colour, Size, Source, SameDayDelivary, NextDayDelivary
from seller.models import Seller
from stock.models import Bach

from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Admin part
from admin_login.models import zaptayAdmin

# Create your views here.

class ProductViewsDetails(TemplateView):
    template_name = 'product.html'
    '''
    def get(self, request, **kwargs):
        print (kwargs)
        return render(request, self.template_name)
    '''

    def get_context_data(self, **kwargs):
        context = dict()
        product_id = self.kwargs.get('product_slug')
        product_list = Product.objects.all().filter(prod_custom_id=product_id)
        product_stock_price = Bach.objects.filter(product_id=product_list[0].id)
        if product_stock_price:
            product_price_dic_percent = int(100-((float(product_stock_price[0].offer_price)/float(product_stock_price[0].main_price))*100))
        else:
            product_price_dic_percent = ""
        context = {'product_all_desc': product_list.first(), 'product_stock_price': product_stock_price.first(), 'price_discount': product_price_dic_percent}
        return context


# ----------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------     Admin Part      ------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------

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

class ViewProduct(TemplateView):
    template_name = 'admin_template/product_form_show.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ViewProduct, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        product_id = self.kwargs.get('product_id')
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        product_list = Product.objects.all().filter(prod_custom_id=product_id).first()
        product_image_list = ProductImage.objects.all().filter(product_id=product_list).order_by('product_img_sl_no')
        context = {"page_name": "product_list", "admin_name": get_name.admin_f_name+" "+get_name.admin_l_name, 'product_details': product_list, 'product_image': product_image_list}
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

            if tertiary_category != "":
                tertiary_category_id_object = TertiaryCategory.objects.all().filter(ter_category_id=tertiary_category).first()
            else:
                tertiary_category_id_object = ""
            color_id_object = Colour.objects.all().filter(color_id=color).first()
            size_id_object = Size.objects.all().filter(size_id=size).first()
            source_id_object = Source.objects.all().filter(source_id=source).first()
            seller_id_object = Seller.objects.all().filter(seller_id=seller).first()
            admin_id = zaptayAdmin.objects.all().filter(email_id=request.session.get('admin_email_id')).first()

            if tertiary_category_id_object == "":
                store_product = Product(
                                prod_title=product_title,
                                prod_category=get_category_id_object,
                                prod_sub_category=sub_category_id_object,
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
            else:
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

            if 'product_image' in request.FILES:
                product_image_array = request.FILES.getlist('product_image')
                # print (product_image_array)
                sl_no = request.POST.getlist('product_sl_image')
                # print (sl_no)
                is_home_image_select = request.POST.getlist('product_home_image')
                # print (is_home_image_select)
                i=0
                for product_image in product_image_array:
                    fs = FileSystemStorage()
                    image_title = product_title+"."+product_image.name.split('.')[-1]
                    image_title = image_title.replace(" ", "")
                    upload_image = fs.save("products/images/"+image_title, product_image)
                    # print (product_image.name)
                    img_url = fs.url(upload_image)
                    mod_image_name = img_url.split("/")[-1]
                    image_path = 'products/images/'+mod_image_name
                    product_sl_no = int(sl_no[i])

                    is_home_image = 0
                    if int(is_home_image_select[0]) == i:
                        is_home_image = 1

                    product_img = ProductImage(prod_image_title=product_title, product_image=image_path, product_img_sl_no=product_sl_no, home_image=is_home_image, added_by=admin_id, product_id=store_product)
                    product_img.save()

                    print (product_title)
                    print (image_path)
                    print (product_sl_no)
                    print (is_home_image)
                    print (admin_id)
                    print (store_product)

                    i=i+1
                    # print (img_url)



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


# ******************************************************************************************************************
# Ajax hendel

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

@csrf_exempt
def SearchByAllCategory(request):
    all_fields_list = list()
    category = request.GET.get('category_id')
    sub_category = request.GET.get('sub_category_id')
    tertiary_category = request.GET.get('tertiary_category_id')

    if category != "" and sub_category != "" and tertiary_category != "":
        # Sorted by category sub category and tertori
        get_data_db = Product.objects.all().filter(prod_category=category, prod_sub_category=sub_category, prod_tertiary_category=tertiary_category)
        for prod_data in get_data_db:
            all_fields = dict()
            # get_category_name = MainCategory.objects.filter(pk = prod_data.prod_category).all()
            category_name = str(prod_data.prod_category)
            all_fields['prod_custom_id'] = prod_data.prod_custom_id
            all_fields['prod_title'] = prod_data.prod_title
            all_fields['prod_category'] = category_name
            all_fields['create_date'] = prod_data.create_date.strftime("%d-%M-%Y")
            all_fields_list.append(all_fields)
        # print (all_fields_list)
        data = {
            'status': 'success',
            'resp': all_fields_list
        }
        return JsonResponse(data)

    elif category != "" and sub_category != "":
        # Sorted by category sub category
        get_data_db = Product.objects.all().filter(prod_category=category, prod_sub_category=sub_category)
        for prod_data in get_data_db:
            all_fields = dict()
            # get_category_name = MainCategory.objects.filter(pk = prod_data.prod_category).all()
            category_name = str(prod_data.prod_category)
            all_fields['prod_custom_id'] = prod_data.prod_custom_id
            all_fields['prod_title'] = prod_data.prod_title
            all_fields['prod_category'] = category_name
            all_fields['create_date'] = prod_data.create_date.strftime("%d-%M-%Y")
            all_fields_list.append(all_fields)
        # print (all_fields_list)
        data = {
            'status': 'success',
            'resp': all_fields_list
        }
        return JsonResponse(data)

    elif category != "":
        # Sorted by category
        get_data_db = Product.objects.all().filter(prod_category=category)
        for prod_data in get_data_db:
            all_fields = dict()
            # print (prod_data.create_date.strftime("%d-%M-%Y"))
            category_name = str(prod_data.prod_category)
            all_fields['prod_custom_id'] = prod_data.prod_custom_id
            all_fields['prod_title'] = prod_data.prod_title
            all_fields['prod_category'] = category_name
            all_fields['create_date'] = prod_data.create_date.strftime("%d-%M-%Y")
            all_fields_list.append(all_fields)
        # print (all_fields_list)
        data = {
            'status': 'success',
            'resp': all_fields_list
        }
        return JsonResponse(data)
    else:
        # All fields
        get_data_db = Product.objects.all()
        for prod_data in get_data_db:
            all_fields = dict()
            # get_category_name = MainCategory.objects.filter(pk = prod_data.prod_category).all()
            category_name = str(prod_data.prod_category)
            all_fields['prod_custom_id'] = prod_data.prod_custom_id
            all_fields['prod_title'] = prod_data.prod_title
            all_fields['prod_category'] = category_name
            all_fields['create_date'] = prod_data.create_date.strftime("%d-%M-%Y")
            all_fields_list.append(all_fields)
        # print (all_fields_list)
        data = {
            'status': 'success',
            'resp': all_fields_list
        }
        return JsonResponse(data)

    data = {
        'status': 'error'
    }
    return JsonResponse(data)


@csrf_exempt
def SearchByID(request):
    all_fields_list = list()
    search_key = request.GET.get('search_key');

    if search_key != "":
        # Sorted by category sub category and tertori
        get_data_db = Product.objects.all().filter(prod_custom_id__icontains=search_key)
        for prod_data in get_data_db:
            all_fields = dict()
            # get_category_name = MainCategory.objects.filter(pk = prod_data.prod_category).all()
            category_name = str(prod_data.prod_category)
            all_fields['prod_custom_id'] = prod_data.prod_custom_id
            all_fields['prod_title'] = prod_data.prod_title
            all_fields['prod_category'] = category_name
            all_fields['create_date'] = prod_data.create_date.strftime("%d-%M-%Y")
            all_fields_list.append(all_fields)
        # print (all_fields_list)
        data = {
            'status': 'success',
            'resp': all_fields_list
        }
        return JsonResponse(data)
    else:
        # All fields
        get_data_db = Product.objects.all()
        for prod_data in get_data_db:
            all_fields = dict()
            # get_category_name = MainCategory.objects.filter(pk = prod_data.prod_category).all()
            category_name = str(prod_data.prod_category)
            all_fields['prod_custom_id'] = prod_data.prod_custom_id
            all_fields['prod_title'] = prod_data.prod_title
            all_fields['prod_category'] = category_name
            all_fields['create_date'] = prod_data.create_date.strftime("%d-%M-%Y")
            all_fields_list.append(all_fields)
        print (all_fields_list)
        data = {
            'status': 'success',
            'resp': all_fields_list
        }
        return JsonResponse(data)

    data = {
        'status': 'error'
    }
    return JsonResponse(data)
