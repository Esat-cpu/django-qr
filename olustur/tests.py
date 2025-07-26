from django.test import TestCase
from django.urls import reverse
from io import BytesIO
import base64

from .utils import Qr


def kodu_base64_al(url) -> str:
    """
    Verilen string bir qr kod png görselinin base64 ile kodlanmış haline çevrilir ve döndürülür.
    """
    buffer = BytesIO()
    Qr(url).save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


class HomeTests(TestCase):
    def test_sayfaya_aciliyor_mu(self):
        """
        Home page başta normal açılır mı kontrolü.
        """
        response = self.client.get(reverse("olustur:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "URL Adresi Girin:")

    def test_url_gir(self):
        """
        Bir metin post ile verildiğinde, kodu_base64_al fonksiyon çıktısı ile sayfanın görsel için
        kullanılan context ögesi karşılaştırılır. QR kod görseli doğru iletildi mi kontrolü.
        """
        url = "deneme/deneme/deneme"
        url64 = kodu_base64_al(url)
        response = self.client.post(reverse("olustur:home"), {"link": url})
        self.assertEqual(response.context["qrkod"], url64)
