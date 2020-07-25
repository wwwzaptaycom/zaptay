from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView

from admin_login.models import zaptayAdmin

from .attribute_forms import CategoryForm, SubcategoryForm, TertiaryCategoryForm

from category.models import MainCategory

# Create your views here.

class AttributeList(FormView):
    template_name = 'admin_template/attributes.html'
    # form_class = CategoryForm
    category_form_class = CategoryForm
    sub_category_form_class = SubcategoryForm
    teri_category_class = TertiaryCategoryForm

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(AttributeList, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        category_list = MainCategory.objects.all()
        context = {"page_name": "attribute", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name, "category_list": category_list}
        context['category_form'] = self.category_form_class
        context['sub_category_form'] = self.sub_category_form_class
        context['tertia_form'] = self.teri_category_class
        return context

    def post(self, request, *args, **kwargs):
        if 'category_add_form' in request.POST:
            category_form = CategoryForm(request.POST)

            if category_form.is_valid():
                category_name = request.POST['category_add_form']
                admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))
                insert_que = MainCategory(main_category_name = category_name, added_by = admin_id)
                insert_que.save()
                messages.success(request, "Catagory added", extra_tags='category')
            else:
                messages.error(request, "All fields mentetory", extra_tags='category')

        if 'sub_category_add_form' in request.POST:
            sub_category_from = SubcategoryForm(request.POST)

            if sub_category_from.is_valid():
                print ("Sub category valid")
            else:
                # select_category = request.POST['']
                messages.error(request, "All fields mentetory", extra_tags='sub_category')

        if 'tert_category_add_form' in request.POST:
            sub_category_from = TertiaryCategoryForm(request.POST)

            if sub_category_from.is_valid():
                print ("Sub category valid")
            else:
                messages.error(request, "All fields mentetory", extra_tags='terriary_category')
        return render(request, self.template_name, self.get_context_data())

    def form_invalid(self, form):
        context = self.get_context_data(task_form=form)
        context['error'] = form
        print (context)
        return self.render_to_response(context)
