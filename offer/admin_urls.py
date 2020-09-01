from django.urls import path, include
from offer import views

app_name = 'offer'

urlpatterns = [
    path('', views.ShowOfferList.as_view(), name="offer_list"),
    path('create-offer', views.ShowOfferForm.as_view(), name="create_offer"),
    path('edit-offer/<slug:offer_id>', views.EditOfferForm.as_view(), name="edit_offer"),



    # Ajax URL
    path('search-product-batch', views.SearchProductBatch, name="search_prduct_batch"),
    path('insert-offer-product', views.InsertOfferProduct, name="insert_offer_product"),
    path('offer-product-list', views.OfferProductLisr, name="offer_product_list"),
]
