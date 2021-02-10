from django.forms import ModelForm
from .models import Order, Car


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
