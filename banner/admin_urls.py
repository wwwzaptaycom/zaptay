from django.urls import path, include
from banner import views

app_name = "banner"

urlpatterns = [
    path('', views.ViewBanner.as_view(), name="banner_list"),
]
