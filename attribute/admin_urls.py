from django.urls import path, include
from attribute import views

app_name = "attribute"

urlpatterns = [
    path('', views.AttributeList.as_view(), name="attribute"),


    # Ajax url
    path('get-cateory', views.SendCategoryData, name="ajax_category"),
    path('get-sub-cateory', views.SendSubCategoryData, name="ajax_sub-category"),
    path('delete-attributes/', views.DeleteAttrinutsData, name="ajax_attribute_del"),
]
