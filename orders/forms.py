from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Order, User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'telegram_username', 'password1', 'password2']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'telegram', 'deadline', 'description', 'media']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2',
                'placeholder': 'Ваше имя'
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2',
                'placeholder': '@ваш_telegram'
            }),
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full border border-gray-300 rounded-md p-2'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2',
                'rows': 4,
                'placeholder': 'Краткое описание задачи'
            }),
            'media': forms.ClearableFileInput(attrs={
                'class': 'w-full'
            }),
        }