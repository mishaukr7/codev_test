from django.test import TestCase

from catalog.models import Seller, Product
from catalog.serializers import SellerWithProductsSerializer, ProductSerializer


class SellerWithProductsSerializerTestCase(TestCase):

    def setUp(self):
        self.product_attributes = {
            'name': 'Asus G500',
            'description': "This is Asus G500 description"
        }

        self.seller_attributes = {
            'name': 'John Smith',
            'birthday': '1990-01-19',
        }

        self.serializer_data = {
            'id': 1,
            'name': 'John Smith',
            'birthday': '1990-01-19',
            'products': [
                {
                    'id': 1,
                    'name': 'Asus G500',
                    'description': "This is Asus G500 description"
                }
            ]
        }

        self.seller = Seller.objects.create(**self.seller_attributes)
        self.product = Product.objects.create(**self.product_attributes, seller=self.seller)

        self.serializer = SellerWithProductsSerializer(self.seller)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['id', 'name', 'birthday', 'products']))


class ProductSerializerTestCase(TestCase):
    def setUp(self):

        self.product_attributes = {
            'name': 'Asus G500',
            'description': "This is Asus G500 description"
        }

        self.seller_attributes = {
            'name': 'John Smith',
            'birthday': '1990-01-19',
        }

        self.seller = Seller.objects.create(**self.seller_attributes)
        self.product = Product.objects.create(**self.product_attributes, seller=self.seller)

        self.serializer = ProductSerializer(self.product)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['id', 'seller', 'name', 'description', 'created', 'updated']))


