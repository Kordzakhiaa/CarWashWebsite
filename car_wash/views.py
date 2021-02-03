from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home.html')


def create_order(request):
    return render(request, 'create_order.html')


def washer_detail(request, pk: int):
    washer_by_id = CarWasher.objects.get(pk=pk)
    filter_by_washer_name = Order.objects.filter(washer__name=washer_by_id.name)
    earned_money = 0
    for i in filter_by_washer_name:
        earned_money += i.order_price
    context = {
        'washer_by_id': washer_by_id,
        'earned_money': earned_money
    }
    return render(request, 'washer_details.html', context)


def order(request):
    orders = Order.objects.all()

    return render(request, 'order.html', {'orders': orders})


def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})
