import unittest

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")

    def test_calculate_sum(self):
        response = self.client.get("/sum/1/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"3")   

    def test_calculate_subtract(self):
        response = self.client.get("/subtract/1/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"-1")

    def test_print_five(self):
        response = self.client.get("/five")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"5")

if __name__ == "__main__":
    unittest.main()
