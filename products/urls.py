from django.urls import path
from .views import ProductViewSet, SaleItemList

urlpatterns = [
    path('products/', ProductViewSet.as_view(), name='product-list'),
    path('api/sale-items/', SaleItemList.as_view(), name='sale-items'),
    # Add more URLs as needed
]
