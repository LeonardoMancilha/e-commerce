from django.test import TestCase
from ..models.Product_Models import Product


class TestProductModels(TestCase):

    def setUp(self):
        self.product = Product(
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

    def test_created_at_is_set_on_create(self):
        product = Product(
            product_name='testing',
            product_slug='testing',
            product_description='This is a testing',
            product_price=100.0
        )
        self.assertIsNone(product.created_at)

        product.save()

        self.assertIsNotNone(product.created_at)

    def test_updated_at_is_set_on_create(self):
        product = Product(
            product_name='testing',
            product_slug='testing',
            product_description='This is a testing',
            product_price=100.0
        )

        self.assertIsNone(product.updated_at)

        product.save()

        self.assertIsNotNone(product.updated_at)

    def test_updated_at_is_set_on_update(self):
        product = Product(
            product_name='testing',
            product_slug='testing',
            product_description='This is a testing',
            product_price=100.0
        )
        product.save()
        updated_at = product.updated_at
        product.save()

        self.assertNotEquals(updated_at, product.updated_at)

    def test_created_at_is_not_set_on_update(self):
        product = Product(
            product_name='testing',
            product_slug='testing',
            product_description='This is a testing',
            product_price=100.0
        )
        product.save()
        created_at = product.created_at
    
        product.save()
        self.assertEquals(created_at, product.created_at)