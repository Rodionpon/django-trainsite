from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    weight = forms.FloatField(required=True, label="Вес (кг)")
    height = forms.FloatField(required=True, label="Рост (см)")
    gender = forms.ChoiceField(choices=[("male", "Мужской"),("female", "Женский")],required=True, label="Пол" )
    birthdate = forms.DateField(required=True, label="Дата рождения")