from django.test import TestCase
from ..models.Product_Models import Product


class TestProductModels(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            product_name='testing_product',
            product_description='This is a testing case.',
            product_price=100.0
        )
        self.product.save()

    def tearDown(self):
        self.product.delete()

    def test_create_a_new_product(self):
        product = self.product
        
        self.assertTrue(product)
        self.assertIsInstance(product, Product)
        self.assertIsNotNone(product)
        self.assertEqual(1, Product.objects.count())

    def test_str_repr_method_returns_the_product_name(self):
        self.assertEqual(str(self.product), self.product.product_name)