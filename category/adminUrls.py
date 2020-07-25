from django.contrib import admin
from django.urls import path

from category import views

app_name = 'category'

urlpatterns = [
    # Admin Part ----------------------------------------------------------------------------------------------------------------------
    path('add-main-category/', views.AddMainCategory.as_view(), name="admin_add_category"),
    path('show-all/', views.ShowAllMainCategory.as_view(), name="admin_show_main_categorypage"),
    path('add-sub-category/', views.AddSubCategory.as_view(), name="admin_add_sub_category"),
]
