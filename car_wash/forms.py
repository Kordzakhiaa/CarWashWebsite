from django.forms import ModelForm, forms, DateTimeField
from .models import Order, Car
from django import forms
from django.forms import EmailField, CharField, Textarea, ModelChoiceField, TextInput


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
