from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class Car(models.Model):
    marka = models.CharField(max_length=50, verbose_name="Марка")
    model = models.CharField(max_length=50, verbose_name="Модель")
    gos_number = models.CharField(max_length=10, verbose_name="Гос номер")
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=True)
    vin_code = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return f"{self.marka} {self.model} ({self.gos_number})"