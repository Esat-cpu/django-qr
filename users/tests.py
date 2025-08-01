from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from olustur.models import URLs


class UserTest(TestCase):
    def setUp(self):
        self.user_passwd = "123456"
        self.user2_passwd = "654321"

        self.user = User.objects.create_user(username="denem", password=self.user_passwd)
        self.user2 = User.objects.create_user(username="denem2", password=self.user2_passwd)

        self.girdi = "asdfasdfasdf"
        self.kayitli_url = URLs.objects.create(url=self.girdi, author=self.user, pk=1)
        self.login_must_url = reverse("olustur:home_with_form", args=("1",))


    def test_giris_yapmadan_erisim(self):
        """
        id'si 1 olan ve 1. user'a ait olan url'ye giriş yapmayan kişiler erişemez.
        """
        response = self.client.get(self.login_must_url)
        self.assertEqual(response.status_code, 302) # login sayfasına yönlendirilir

    
    def test_kayitli_urlye_erisim(self):
        """
        id'si 1 olan ve 1. user'a ait olan url'ye 1. user erişebilir.
        """
        login = self.client.login(username=self.user.username, password=self.user_passwd)
        self.assertTrue(login)

        response = self.client.get(self.login_must_url)
        self.assertEqual(response.status_code, 200)


    def test_farkli_kullanici_erisim(self):
        """
        id'si 1 olan ve 1. user'a ait olan url'ye 2. user erişemez. Ve 404 sayfasına yönlendirilir.
        """
        login = self.client.login(username=self.user2.username, password=self.user2_passwd)
        self.assertTrue(login)

        response = self.client.get(self.login_must_url)
        self.assertEqual(response.status_code, 404)
