from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=7, choices=[("male", "Мужской"),("female", "Женский")], null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)