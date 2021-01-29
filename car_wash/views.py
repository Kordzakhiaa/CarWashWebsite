from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home.html')


def order(request):
    orders = Order.objects.all()
    return render(request, 'order.html', {'orders': orders})


def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})


def carwasher(request):
    car_washers = CarWasher.objects.all()
    return render(request, 'carwasher.html', {'car_washers': car_washers})
