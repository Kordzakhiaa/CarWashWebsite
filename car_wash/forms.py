from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Order, Car
from django import forms


class OrderForm(ModelForm):
    order_start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    order_end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Order
        fields = '__all__'


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Repeat your password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
