from django.test import TestCase

from catalog.models import Seller, Product


class SellerTestCase(TestCase):
    """ Test module for Seller model """

    def setUp(self):
        Seller.objects.create(
            name='John Smith',
            birthday='1990-01-19'
        )
        Seller.objects.create(
            name='Tom Krus',
            birthday='1923-03-19'
        )

    def test_name_label(self):
        seller = Seller.objects.get(id=1)
        field_label = seller._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Seller name')

    def test_birthday_label(self):
        seller = Seller.objects.get(id=1)
        field_label = seller._meta.get_field('birthday').verbose_name
        self.assertEquals(field_label, 'Seller birthday')

    def test_name_max_length(self):
        author = Seller.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)


class ProductTestCase(TestCase):
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

    def test_seller_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('seller').verbose_name
        self.assertEquals(field_label, 'Seller')

    def test_seller_relationship(self):
        seller = Seller.objects.get(id=1)
        product = Product.objects.get(id=1)
        self.assertEqual(product.seller, seller)

    def test_seller_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('seller').verbose_name
        self.assertEquals(field_label, 'Seller')

    def test_name_max_length(self):
        author = Seller.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
