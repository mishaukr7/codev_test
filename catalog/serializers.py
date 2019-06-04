from rest_framework import serializers

from catalog.models import Product, Seller


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'seller',
            'name',
            'description',
            'created',
            'updated',
        )
        read_only_fields = (
            'id',
            'created',
            'updated'
        )


class SellerWithProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = (
            'id',
            'name',
            'birthday',
            'products'
        )

        read_only_fields = (
            'id',
        )
