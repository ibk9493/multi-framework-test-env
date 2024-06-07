import unittest
from src.app import create_app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Flask code runs successfully!', response.data)

if __name__ == "__main__":
    unittest.main()
