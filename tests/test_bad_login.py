from django.contrib.auth.models import User
from django.test import TestCase


class PurchaseTest(TestCase):
    def setUp(self):
        User.objects.create_user(username="bill", password="gates")

    def test_correct_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        response = self.client.post(response.url, {
            "username": "bill",
            "password": "gates",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

    def test_incorrect_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        response = self.client.post(response.url, {
            "username": "bill",
            "password": "not_gates",
        })
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
