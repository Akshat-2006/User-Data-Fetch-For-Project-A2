from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField()
    phone = models.FloatField(max_length=10)
    ref_id = models.CharField(max_length=20)
    ver_id = models.FloatField(max_length=8)
