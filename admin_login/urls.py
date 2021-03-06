from django.urls import path, include

from admin_login import views

app_name = "admin_login"

urlpatterns = [
    path('login/', views.ShowadminLoginView.as_view(), name="admin_loginpage"),
    path('logout/', views.ShowadminLogoutView.as_view(), name="admin_logoutpage"),
    path('dashboard/', views.ShowadminDashboardView.as_view(), name="admin_dashboardpage"),
    path('attribute/', include('attribute.admin_urls')),
    path('product/', include('product.admin_urls')),
    path('seller/', include('seller.admin_urls')),
    path('banner/', include('banner.admin_urls')),
    path('stock/', include('stock.admin_urls')),
    path('offer/', include('offer.admin_urls')),



    # path('category/', include('category.adminUrls'))
    # path('category/', views.ShowAllMainCategory.as_view(), name="admin_show_main_categorypage"),
]
