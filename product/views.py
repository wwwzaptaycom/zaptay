from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, ListView

from .product_form import ProductForm

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
        context = {"page_name": "product_list", "admin_name": get_name.admin_f_name+" "+get_name.admin_l_name}
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
            return redirect('/site-admin/product/product-form')
            # return redirect('admin_login:admin_loginpage')
    '''

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "add_product", "admin_name": get_name.admin_f_name+" "+get_name.admin_l_name, 'form': self.form_class}
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            prodict_title = request.POST['product_title']
            main_price = request.POST['main_price']
            offer_price = request.POST['offer_price']
            extra_price = request.POST['extra_price']
            purchase_price = request.POST['purchase_price']
            category = request.POST['category']
            sub_category = request.POST['sub_cateegory']
            tertiary_category = request.POST['tertiary']
            prod_desc = request.POST['description']
            color = request.POST['color']
            size = request.POST['size']
            source = request.POST['made_in']
            youtube = request.POST['youtube']

            weekly_dreals=top_offer=free_shiping=return_product=cod =0
            if 'weekly_dreals' in request.POST:
                weekly_dreals = request.POST['weekly_dreals']
            if 'top_offer' in request.POST:
                top_offer = request.POST['top_offer']
            if 'free_shiping' in request.POST:
                free_shiping = request.POST['free_shiping']
            if 'return_product' in request.POST:
                return_product = request.POST['return_product']
            if 'cod' in request.POST:
                cod = request.POST['cod']

            print ("*********************************************************************************")
            print (prodict_title,mrp_price,selling_price,extra_discount,category,sub_category,tertiary_category,prod_desc,color,size,source,youtube,weekly_dreals,top_offer,free_shiping,return_product,cod)

            return self.form_valid(form)
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
