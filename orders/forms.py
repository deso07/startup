from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Order, User
from datetime import date

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'telegram_username', 'password1', 'password2']

class OrderForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дедлайн'
    )

    class Meta:
        model = Order
        fields = ['name', 'telegram', 'deadline', 'description', 'media']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название заказа',
                'style': 'font-family: Montserrat, sans-serif;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите ваш заказ',
                'style': 'font-family: Montserrat, sans-serif;'
            }),
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'style': '''
                    font-family: Montserrat, sans-serif;
                    background-color: white;
                    border: 2px solid #E5E7EB;
                    border-radius: 1rem;
                    padding: 0.75rem;
                    width: 100%;
                    cursor: pointer;
                ''',
                'min': date.today().strftime('%Y-%m-%d')
            }),
            'media': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'font-family: Montserrat, sans-serif;'
            })
        }