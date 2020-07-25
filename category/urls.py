from django.contrib import admin
from django.urls import path

from category import views

app_name = 'category'

urlpatterns = [
    path('men/', views.CategoryViews.as_view(), name="category-men"),
    path('men/<slug:product_slug>/', views.ProductViews.as_view(), name="category-men"),


    # Admin Part ----------------------------------------------------------------------------------------------------------------------
    # path('add-main-category/', views.AddMainCategory.as_view(), name="admin_add_category"),
    # path('show-all/', views.ShowAllMainCategory.as_view(), name="admin_show_main_categorypage"),
    # It's moves on adminUrls.py
]
