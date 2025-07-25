from django.test import TestCase
from django.urls import reverse

class HomeTests(TestCase):
    def test_sayfaya_aciliyor_mu(self):
        response = self.client.get(reverse("olustur:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "URL Adresi Girin:")
