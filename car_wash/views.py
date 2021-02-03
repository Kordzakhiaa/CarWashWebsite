from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home.html')


def create_order(request):
    return render(request, 'create_order.html')


def washer_detail(request, pk: int):
    washer_by_id = CarWasher.objects.get(pk=pk)
    order_count = washer_by_id.orders.all().count()
    orders = Order.objects.values_list('order_price')
    context = {
        'washer_by_id': washer_by_id,
        'order_count': order_count,
        'orders': orders,
    }
    return render(request, 'washer_details.html', context)


def order(request):
    orders = Order.objects.all()
    return render(request, 'order.html', {'orders': orders})


def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})


def carwasher(request):
    car_washers = CarWasher.objects.all()
    return render(request, 'carwasher.html', {'car_washers': car_washers})
