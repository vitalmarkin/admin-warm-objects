from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product
from .serializers import ProductSerializer


class ProductListAPI(ListAPIView):
    queryset = Product.objects.filter(status='published', show_on_main=True)
    serializer_class = ProductSerializer


class ProductDetailAPI(RetrieveAPIView):
    queryset = Product.objects.filter(status='published')
    serializer_class = ProductSerializer
    lookup_field = 'slug'