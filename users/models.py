from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class URLs(models.Model):
    url = models.TextField() # girdi url olmak zorunda değil
    tarih =  models.DateTimeField("Kullanıldığı tarih", default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-tarih"]
        verbose_name = "metin"
        verbose_name_plural = "metinler"
        db_table = "girilen_urls"

    def __str__(self):
        return f"{self.author.username}:{self.url[:10]}"
