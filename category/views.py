from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import View, TemplateView, FormView

# Create your views here.

class CategoryViews(TemplateView):
    template_name = 'category.html'

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
