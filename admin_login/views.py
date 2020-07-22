from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, FormView

from .login_form import LoginForm

from admin_login.models import zaptayAdmin

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
