from django.urls import path, include, re_path
from seller import views

app_name = "seller"

urlpatterns = [
    path('all-seller/', views.ViewSellerList.as_view(), name="all_seller"),
    path('seller-view/<slug:seller_id>', views.ViewSeller.as_view(), name="seller_view"),
    path('add-seller/', views.AddSellerForm.as_view(), name="add_seller"),
]
