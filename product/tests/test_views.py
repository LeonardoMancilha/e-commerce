from django.test import TestCase
from django.urls import reverse


class TestProductViews(TestCase):

    def test_product_endpoint_request_must_return_200(self):
        response = self.client.get(reverse('view_products'))
        self.assertEqual(response.status_code, 200)

    def test_nonexistent_product_endpoint_request_must_return_404_page_not_fount(self):
        response = self.client.get('nonexistent_endpoint')
        self.assertEqual(response.status_code, 404)

    def test_product_template_used_must_return_200(self):
        self.assertTemplateUsed('products.html')
    