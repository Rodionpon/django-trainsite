from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=7, choices=[("male", "Мужской"),("female", "Женский")], null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True
    )
