from django.urls import path, include
from product import views

app_name = 'product'

urlpatterns = [
    path('', views.ShowProductList.as_view(), name="product_list"),
    path('product-form', views.ShowProductForm.as_view(), name="product_form"),
    path('<slug:product_id>', views.ViewProduct.as_view(), name="product_show"),

    # Ajax URLField
    path('search-product/', views.SearchByAllCategory, name="search_product"),
    path('search-product-id/', views.SearchByID, name="search_product_id"),
]
