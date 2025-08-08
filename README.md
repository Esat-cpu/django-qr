# Django-QR

Kullanıcıdan alınan url adresini qr koda çevirip kullanıcıya sunan bir django web uygulaması.

---

## Özellikler

- Kolay şekilde QR kod oluşturma
- Basit ve temiz arayüz
- Kullanıcı giriş sistemi ve profil fotoğrafı ekleme.

---

## Kurulum

```bash
git clone https://github.com/Esat-cpu/django-qr.git
cd django-qr
```

---

Öncelikle .env.example dosyasından hareketle bir .env dosyası oluşturun:
- Django projesi için bir secret key belirleyin. DEBUG değerini ayarlayın (production ortamında False olmalı).
- Bir PostgreSQL url'si yazın ve POSTGRES_DB, POSTGRES_USER ve POSTGRES_PASSWORD kısımlarını ona göre girin.
- Uygulamanın e-posta yollayabilmesi için geçerli bir e-mail adresi ve e-mail uygulama parolasını girin.

---

Windows için:
```powershell
.\setup.bat
```

Linux veya macOS için:
```bash
./setup.sh
```
> **Not:** Bu projeyi çalıştırmak için sisteminizde Docker Desktop veya ayrı olarak Docker ve Docker Compose kurulu olmalıdır.

---

### Container'ları durdurmak için
```bash
docker-compose stop
```

### Tekrar başlatmak için
Windows için:
```powershell
.\start.bat
```
Linux veya macOS için:
```bash
./start.sh
```
