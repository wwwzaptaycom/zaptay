from django.urls import path, include

from admin_login import views

urlpatterns = [
    path('login/', views.ShowadminLoginView.as_view(), name="admin_loginpage"),
    path('dashboard/', views.ShowadminDashboardView.as_view(), name="admin_dashboardpage"),
]
