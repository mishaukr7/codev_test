from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from catalog.models import Product, Seller
from catalog.serializers import SellerWithProductsSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )

    def get_serializer_class(self):
        if self.action == 'sellers_with_products':
            return SellerWithProductsSerializer
        return ProductSerializer

    def get_queryset(self):
        if self.action == 'sellers_with_products':
            return Seller.objects.all()
        return Product.objects.all()

    @action(detail=False, methods=['GET'], )
    def sellers_with_products(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

