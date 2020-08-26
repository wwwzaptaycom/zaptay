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
        category_name = self.kwargs.get('category')
        terti_category_details = TertiaryCategory.objects.filter(sub_category_id__in=Subquery(
                            SubCategory.objects.filter(sub_category_name=category_name).values('sub_category_id')))
        # print (terti_category_details)
        context = {"tertiary_category":terti_category_details,
                    "category_name": category_name}
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
