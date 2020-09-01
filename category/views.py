from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView

from django.db.models import Subquery, Q

from .models import MainCategory
from banner.models import Banner
from attribute.models import SubCategory, TertiaryCategory
from product.models import Product, ProductImage
from stock.models import Bach

# Admin part
from admin_login.models import zaptayAdmin
# from . add_main_category_form import AddMainCategoryForm
from . category_forms import AddMainCategoryForm, AddSubCategoryForm

# Create your views here.

class CategoryViews(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = dict()
        category_name = self.kwargs.get('category').replace("_", " ")
        tertiarycategory_name = self.kwargs.get('tertiarycategory')
        # print (tertiarycategory_name)
        # print (category_name)

        # Get banner
        banner_category = ""
        if category_name == "men":
            banner_category = "men_banner"
        elif category_name == "women":
            banner_category = "women_banner"

        if banner_category != '':
            category_banner = Banner.objects.filter(banner_name=banner_category).values('id', 'banner_image', 'banner_link')
        else:
            category_banner = ""

        if tertiarycategory_name == None:
            terti_category_details = TertiaryCategory.objects.filter(sub_category_id__in=Subquery(
                                SubCategory.objects.filter(sub_category_name=category_name).values('sub_category_id')))
            # print (terti_category_details)
            context = {"tertiary_category":terti_category_details,
                        "category_name": category_name,
                        "banner":category_banner}
        else:
            tertiary_category_list = list()
            terti_category_details = TertiaryCategory.objects.filter(ter_category_name=tertiarycategory_name).first()
            terti_category_details_all = TertiaryCategory.objects.filter(sub_category_id__in=Subquery(
                                SubCategory.objects.filter(sub_category_name=category_name).values('sub_category_id'))).exclude(ter_category_id= terti_category_details.ter_category_id)
            # print (terti_category_details)
            # print (terti_category_details1)
            tertiary_category_list.append({'ter_category_id': terti_category_details.ter_category_id, 'ter_category_name': terti_category_details.ter_category_name})
            for tertiary_category in terti_category_details_all:
                tertiary_category_dict = dict()
                tertiary_category_dict['ter_category_id'] = tertiary_category.ter_category_id
                tertiary_category_dict['ter_category_name'] = tertiary_category.ter_category_name

                tertiary_category_list.append(tertiary_category_dict)

            # print (tertiary_category_list)
            context = {"tertiary_category":tertiary_category_list,
                        "category_name": category_name,
                        "banner":category_banner}
        return context

class ProductViews(TemplateView):
    template_name = 'product.html'

    # def dispatch(self, request, *args, **kwargs):
    #     print (args, kwargs)
    #
    #     # return super(self)
    #     a = self.kwargs['product_name']
    #     return a

    def get(self, request, **kwargs):
        # <view logic>
        # return super()
        # return HttpResponse(self.template_name)
        print (kwargs)
        return render(request, self.template_name)

# Get Ajax data
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

@csrf_exempt
def ProductFetch(request):
    tertiary_id = request.GET.get('tertiary_id')
    tertiary_name = request.GET.get('tertiary_name')

    # Fetch product by tertiary category
    product_list = list()
    product_list_db = Product.objects.filter(prod_tertiary_category=tertiary_id)
    for product in product_list_db:
        product_dict = dict()
        product_dict['id'] = product.prod_custom_id
        product_dict['name'] = product.prod_title
        product_image_db = ProductImage.objects.filter(product_id=product, home_image=True)
        if product_image_db:
            product_dict['image_path'] = str(product_image_db[0].product_image)
            product_dict['image_title'] = str(product_image_db[0].prod_image_title)
        else:
            product_dict['image_path'] = ''
            product_dict['image_title'] = product.prod_title
        # print (product_image_db)
        product_price_list_db = Bach.objects.filter(product_id=product)
        if product_price_list_db:
            product_dict['product_main_price'] = product_price_list_db[0].main_price
            product_dict['product_offer_price'] = product_price_list_db[0].offer_price
            product_dict['product_price_save'] = int(float(product_price_list_db[0].main_price)-float(product_price_list_db[0].offer_price))
            product_dict['product_price_off_percent'] = int(100-((float(product_price_list_db[0].offer_price)/float(product_price_list_db[0].main_price))*100))
        else:
            product_dict['product_main_price'] = ''
            product_dict['product_offer_price'] = ''
            product_dict['product_price_save'] = ''
            product_dict['product_price_off_percent'] = ''

        product_list.append(product_dict)
    # print (product_list)

    data = {
        'status': 'success',
        'resp': product_list
    }
    return JsonResponse(data)

# Admin part -----------------------------------------------------------------------------------------------------------------------

class AddMainCategory(FormView):
    template_name = 'admin_template/main_category_form.html'
    form_class = AddMainCategoryForm
    success_url = '/site-admin/category/add-main-category/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(AddMainCategory, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "main_category", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, "form": self.form_class}
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            try:
                category_name = request.POST['category_name']
                context = self.get_context_data(task_form=form)
                context['success'] = "success"
                # return self.form_valid(form) #THIS IS 100% OK

                # Insert into database
                admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))
                add_main_category = MainCategory(main_category_name=category_name, added_by=admin_id)
                add_main_category.save()
                return self.render_to_response(context)
            except Exception as e:
                print (e)
                return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data(task_form=form)
        context['error'] = form
        return self.render_to_response(context)

# ========================================================================================================================
class ShowAllMainCategory(TemplateView):
    template_name = 'admin_template/show_all_main_category.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ShowAllMainCategory, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        # Fetch data
        main_cartegory_data = MainCategory.objects.all().order_by('-category_id')
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "main_category", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, "main_category": main_cartegory_data}
        return context



# =======================================================================================================================

class AddSubCategory(FormView):
    template_name = 'admin_template/sub_category_form.html'
    form_class = AddSubCategoryForm
    success_url = '/site-admin/category/add-sub-category/'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(AddSubCategory, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "main_category", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, "form": self.form_class}
        return context

    def form_invalid(self, form):
        context = self.get_context_data(task_form=form)
        context['error'] = form
        return self.render_to_response(context)
