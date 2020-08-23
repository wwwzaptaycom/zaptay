from django.urls import path, include
from stock import views

app_name = 'stock'

urlpatterns = [
    path('', views.ShowStockList.as_view(), name="stock_list"),
    path('add-stock/', views.StockAddForm.as_view(), name="stock_add"),

    # AJAX URL
    path('search-product', views.SearchProduct, name="search_product"),
    path('view-product', views.ViewProduct, name="view_peoduct"),
]
