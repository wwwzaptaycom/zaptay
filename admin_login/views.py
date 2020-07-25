from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView

from .login_form import LoginForm

from admin_login.models import zaptayAdmin

from django.contrib.auth import logout

# Create your views here.

class ShowadminLoginView(FormView):
    form_class = LoginForm
    template_name = 'admin_template/login.html'
    success_url = '/site-admin/dashboard'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            try:
                email_id = request.POST['email_id']
                pwd = request.POST['password']

                # data = zaptayAdmin.objects.all()
                # data = zaptayAdmin.objects.all().filter(password='1234')
                data = zaptayAdmin.objects.all().get(email_id=email_id, password=pwd)

                # Set Session
                request.session['admin_email_id'] = data.email_id
                request.session.set_expiry(0)
                return self.form_valid(form)
            except Exception as e:
                print (e)
                context = {"db_error": "Authentication failure",'form':form}
                return self.render_to_response(context)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data(task_form=form)
        return self.render_to_response(context)

class ShowadminDashboardView(TemplateView):
    template_name = 'admin_template/dashboard.html'

    '''
    def get(self, request, *args, **kwargs):
        if self.request.session['admin_email_id']:
            context = dict()
            context = {"page_name": "dashboard"}
            return render(request, self.template_name, context)
        else:
            return HttpResponseRedirect('/site-admin/login')
    '''
    '''
    def view(request, *args, **kwargs):
        # return self.dispatch(request, *args, **kwargs)
    '''

    def dispatch(self, request, *args, **kwargs):
        # if self.request.session['admin_email_id']:
        #     return super(ShowadminDashboardView, self).dispatch(request, *args, **kwargs)
        # else:
        #     return redirect('/site-admin/login')
        try:
            resp = request.session['admin_email_id']
            return super(ShowadminDashboardView, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return redirect('/site-admin/login')

    def get_context_data(self, **kwargs):
        # print (self.request.session['admin_email_id'])
        # context = super().get_context_data(**kwargs)
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = dict()
        context = {"page_name": "dashboard", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name}
        return context


class ShowAllMainCategory(TemplateView):
    template_name = 'admin_template/show_all_main_category.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(ShowAllMainCategory, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        context = {"page_name": "main_category", "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name}
        return context


class ShowadminLogoutView(TemplateView):
    template_name = 'admin_template/login.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            logout(request)
            del(request.session['admin_email_id'])
            # return super(ShowadminLogoutView, self).dispatch(request, *args, **kwargs)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')
