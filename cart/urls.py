from django.urls import path, include
from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartListView.as_view(), name="show_cartlist"),
]
