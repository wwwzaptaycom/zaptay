from django.urls import path, include
from wishlist import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.WishListView.as_view(), name="show_wishlist"),
]
