import unittest
from app import app, db
from models import Order, Product

class PaginationTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_pagination_orders(self):
        response = self.client.get('/orders?page=1&per_page=10')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('orders', data)
        self.assertIn('total', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)

    def test_pagination_products(self):
        response = self.client.get('/products?page=2&per_page=5')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('products', data)
        self.assertIn('total', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)

if __name__ == '__main__':
    unittest.main()
