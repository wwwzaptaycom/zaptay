from django.contrib import admin
from django.urls import path

from category import views

app_name = 'category'

urlpatterns = [
    # Ajax URL
    path('get-product/', views.ProductFetch, name="fetch_product"),
    # Ajax URL END

    path('<slug:category>/', views.CategoryViews.as_view(), name="category_name"),
    path('<slug:category>/<slug:tertiarycategory>/', views.CategoryViews.as_view(), name="tertiarycategory_name"),
    # path('men/<slug:product_slug>/', views.ProductViews.as_view(), name="category-men"),

    # Admin Part ----------------------------------------------------------------------------------------------------------------------
    # path('add-main-category/', views.AddMainCategory.as_view(), name="admin_add_category"),
    # path('show-all/', views.ShowAllMainCategory.as_view(), name="admin_show_main_categorypage"),
    # It's moves on adminUrls.py
]
