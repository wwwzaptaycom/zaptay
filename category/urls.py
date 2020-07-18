from django.contrib import admin
from django.urls import path

from category import views

app_name = 'category'

urlpatterns = [
    path('/men/', views.CategoryViews.as_view(), name="category-men"),
    path('/men/<slug:product_slug>', views.ProductViews.as_view(), name="category-men"),
]
