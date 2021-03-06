from django.contrib import admin
from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    # path('men/<slug:product_slug>/', views.ProductViews.as_view(), name="category-men"),
    path('add-wish-list/', views.AddWishlist, name="add_wish_list"),
    path('add-to-cart/', views.AddCart, name="add_to_cart"),
    path('<slug:product_slug>/', views.ProductViewsDetails.as_view(), name="show_product"),
]
