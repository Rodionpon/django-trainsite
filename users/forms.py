from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    weight = forms.FloatField(required=True, label="Вес (кг)")
    height = forms.FloatField(required=True, label="Рост (см)")
    gender = forms.ChoiceField(choices=[("male", "Мужской"),("female", "Женский")],required=True, label="Пол" )
    birthdate = forms.DateField(required=True, label="Дата рождения")


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'weight', 'height', 'gender', 'birthdate')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.weight = self.cleaned_data.get('weight')
        user.height = self.cleaned_data.get('height')
        user.gender = self.cleaned_data.get('gender')
        user.birthdate = self.cleaned_data.get('birthdate')
        if commit:
            user.save()
        return user
