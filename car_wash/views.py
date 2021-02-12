from datetime import datetime

from .forms import OrderForm, CarForm
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from car_wash.get_date import date


def home(request):
    return render(request, 'home.html')


def washer_detail(request, pk: int):
    washer_by_id = CarWasher.objects.get(pk=pk)
    filter_by_washer_name = Order.objects.filter(washer__name=washer_by_id.name)
    earned_money = 0
    for i in filter_by_washer_name:
        earned_money += i.order_price
    orders = washer_by_id.orders.all()
    today = datetime.today()
    context = {
        'washer_by_id': washer_by_id,
        'earned_money': earned_money,
        'today': orders.filter(created_date__range=[date(1), today]).count(),
        'weekly': orders.filter(created_date__range=[date(7), today]).count(),
        'monthly': orders.filter(created_date__range=[date(30), today]).count(),
        'yearly': orders.filter(created_date__range=[date(365), today]).count()
    }
    return render(request, 'washer_details.html', context)


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


def cars_list(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})


def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})


def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_wash:order_list')

    return render(request, 'order_form.html', {'form': form})


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('car_wash:order_list')

    context = {'form': form}
    return render(request, 'order_form.html', context)


def delete_order(request, pk: int):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('car_wash:order_list')
    context = {'order': order}
    return render(request, 'delete.html', context)


# def search(request):
#     washer_q = Q()
#     q = request.GET.get('q')
#
#     if q:
#         washer_q &= Order.objects.filter(Q(washer__name__icontains=q))
#     return render(request, 'order_list.html', {'names': washer_q})


def add_car(request):
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_wash:create_order')

    return render(request, 'add_car.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
