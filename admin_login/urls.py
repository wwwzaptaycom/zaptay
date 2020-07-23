from django.urls import path, include

from admin_login import views

app_name = "admin_login"

urlpatterns = [
    path('login/', views.ShowadminLoginView.as_view(), name="admin_loginpage"),
    path('logout/', views.ShowadminLogoutView.as_view(), name="admin_logoutpage"),
    path('dashboard/', views.ShowadminDashboardView.as_view(), name="admin_dashboardpage"),
    path('category/', views.ShowAllMainCategory.as_view(), name="admin_show_main_categorypage"),
]
