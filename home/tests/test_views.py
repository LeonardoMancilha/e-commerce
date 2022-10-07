from django.test import TestCase

class TestHomeView(TestCase):

    def test_simple_request_must_return_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_view_return_home_template(self):
        self.assertTemplateUsed('home/home.html')

    def test_page_not_found_must_return_404_error(self):
        response = self.client.get('index')
        self.assertEqual(response.status_code, 404)