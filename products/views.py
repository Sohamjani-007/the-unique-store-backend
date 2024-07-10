# products/views.py
from rest_framework import viewsets, generics
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
