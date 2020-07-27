from django.urls import path, include
from attribute import views

app_name = "attribute"

urlpatterns = [
    path('', views.AttributeList.as_view(), name="attribute"),
]
