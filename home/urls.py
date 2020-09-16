from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.Home2.as_view(), name="homepage2"),
    path('wish-list/', include('wishlist.urls')),
    path('cart-list/', include('cart.urls')),
]
