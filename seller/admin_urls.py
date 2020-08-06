from django.urls import path, include, re_path
from seller import views

app_name = "seller"

urlpatterns = [
    path('add-seller/', views.AddSellerForm.as_view(), name="add_seller"),
]
