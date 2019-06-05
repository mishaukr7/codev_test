from django.test import TestCase, Client
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

from catalog.models import Seller, Product
from catalog.views import ProductViewSet

client = Client()


class GetAllProductsTestCase(TestCase):
    def setUp(self):
        seller = Seller.objects.create(
            name='John Smith',
            birthday='1990-01-19'
        )

        Product.objects.create(
            seller=seller,
            name='Asus G500',
            description="This is Asus G500 description"
        )
        Product.objects.create(
            seller=seller,
            name='HP Pavilion S51',
            description="This is HP Pavilion S51 description"
        )

        self.factory = APIRequestFactory()

    def test_get_all_products(self):
        view = ProductViewSet.as_view(actions={'get': 'list'})
        request = self.factory.get('catalog:api_catalog_products_list')
        response = view(request)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_text, 'OK')

    def test_get_product_detail(self):
        view = ProductViewSet.as_view(actions={'get': 'retrieve'})
        request = self.factory.get('catalog:api_catalog_products_read')
        response = view(request, pk=1)
        bad_response = view(request, pk=10)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_text, 'OK')
        self.assertNotEqual(bad_response.status_code, 200)

    def test_get_seller_with_products(self):
        view = ProductViewSet.as_view(actions={'get': 'sellers_with_products'})
        request = self.factory.get('catalog:api_catalog_products_sellers_with_products')
        response = view(request)
        self.assertEqual(response.status_code, 200)


class CreateAllProductsTestCase(TestCase):

    def setUp(self):

        self.invalid_product_attributes = {
            'name': 'John Smith',
            'birthday': '1990-01-19',
        }

        self.seller_attributes = {
            'id': 1,
            'name': 'John Smith',
            'birthday': '1990-01-19',
        }

        self.seller = Seller.objects.create(**self.seller_attributes)

        self.product_attributes = {
            'seller': 1,
            'name': 'Asus G500',
            'description': "This is Asus G500 description"
        }

        self.factory = APIRequestFactory()

    def test_create_valid_product(self):
        # api_catalog_products_create
        view = ProductViewSet.as_view(actions={'post': 'create'})
        request = self.factory.post(
            'catalog:api_catalog_products_create',
            data=self.product_attributes,
        )
        response = view(request)
        self.assertEqual(response.status_code, 201)

    def test_create_invalid_product(self):
        view = ProductViewSet.as_view(actions={'post': 'create'})
        request = self.factory.post(
            'catalog:api_catalog_products_create',
            data=self.invalid_product_attributes,
        )
        response = view(request)
        self.assertNotEqual(response.status_code, 201)


class UpdateAllProductsTestCase(TestCase):
    def setUp(self):
        self.product_attributes = {
            'seller': 1,
            'name': 'Asus G500',
            'description': "This is Asus G500 description"
        }

        self.invalid_product_attributes = {
            'name': 'John Smith',
            'birthday': '1990-01-19',
        }

        self.seller_attributes = {
            'id': 1,
            'name': 'John Smith',
            'birthday': '1990-01-19',
        }

        self.seller = Seller.objects.create(**self.seller_attributes)
        self.product = Product.objects.create(seller=self.seller, name='Test name', description='Test description')

        self.factory = APIRequestFactory()

    def test_valid_update_product(self):
        view = ProductViewSet.as_view(actions={'post': 'update'})
        request = self.factory.post(
            'catalog:api_catalog_products_create',
            data=self.product_attributes,
        )
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_invalid_update_product(self):
        view = ProductViewSet.as_view(actions={'post': 'update'})
        request = self.factory.post(
            'catalog:api_catalog_products_create',
            data=self.invalid_product_attributes,
        )
        response = view(request, pk=1)
        self.assertNotEqual(response.status_code, 200)

    def test_invalid_update_wrong_key(self):
        view = ProductViewSet.as_view(actions={'post': 'update'})
        request = self.factory.post(
            'catalog:api_catalog_products_create',
            data=self.invalid_product_attributes,
        )
        response = view(request, pk=10)
        self.assertEqual(response.status_code, 404)


class DeleteProductTestCase(TestCase):
    def setUp(self):
        self.seller = Seller.objects.create(
            name='John Smith',
            birthday='1990-01-19'
        )

        Product.objects.create(
            id=1,
            seller=self.seller,
            name='Asus G500',
            description="This is Asus G500 description"
        )
        Product.objects.create(
            id=2,
            seller=self.seller,
            name='HP Pavilion S51',
            description="This is HP Pavilion S51 description"
        )

        self.factory = APIRequestFactory()

    def test_valid_delete_product(self):
        view = ProductViewSet.as_view(actions={'delete': 'destroy'})
        request = self.factory.delete(
            'catalog:api_catalog_products_delete',
        )
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 204)

    def test_invalid_delete_product(self):
        view = ProductViewSet.as_view(actions={'delete': 'destroy'})
        request = self.factory.delete(
            'catalog:api_catalog_products_delete',
        )
        response = view(request, pk=10)
        self.assertEqual(response.status_code, 404)

