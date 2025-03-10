from rest_framework import viewsets

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # GET, POST, PUT, PATCH, DELETE

    authentication_classes = []
    permission_classes = []
