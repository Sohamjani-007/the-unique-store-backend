from .models import Product
from .serializers import ProductSerializer
from .serializers import SaleItemSerializer
from rest_framework import generics
from .models import SaleItem
from rest_framework.pagination import PageNumberPagination


class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SaleItemPagination(PageNumberPagination):
    page_size = 80


class SaleItemList(generics.ListAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
    pagination_class = SaleItemPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        print(context)
        return context
