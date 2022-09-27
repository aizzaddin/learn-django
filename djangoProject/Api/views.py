from rest_framework import generics

from Supermarket.models import Product
from .serializers import ProductSerializer


class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
