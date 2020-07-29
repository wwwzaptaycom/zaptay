from django.urls import path, include
from product import views

app_name = 'product'

urlpatterns = [
    path('', views.ShowProductList.as_view(), name="product_list"),
    path('product-form', views.ShowProductForm.as_view(), name="product_form"),
]
