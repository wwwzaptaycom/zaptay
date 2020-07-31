from django.urls import path, include, re_path
from attribute import views

app_name = "attribute"

urlpatterns = [
    path('', views.AttributeList.as_view(), name="attribute"),


    # Ajax url
    path('get-cateory', views.SendCategoryData, name="ajax_category"),
    path('get-sub-cateory', views.SendSubCategoryData, name="ajax_sub-category"),
    path('delete-attributes/', views.DeleteAttrinutsData, name="ajax_attribute_del"),

    path('get-sorted-sub-category/', views.SendSortSubCategory, name='sort_sub_category'),
    path('get-sorted-terti-category/', views.TertiarySubCategory, name='sort_terti_category'),
    # re_path(r'^get-sorted-sub-category/(?P<category_id>[0-9])/$', views.SendSortSubCategory, name='sort_sub_category'),
]
