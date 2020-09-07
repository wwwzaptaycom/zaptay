from django.urls import path, include
from user_login import views

app_name = "user_login"

urlpatterns = [
    path('signup/', views.UserSignUp, name="user_signup"),
    path('signin/', views.UserSignIn, name="user_signin"),
]
