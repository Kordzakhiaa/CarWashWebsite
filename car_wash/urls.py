from .views import *
from django.urls import path

urlpatterns = [
    path('', name='home', view=home),
    path('order/', name='order', view=order),
    path('customers/', name='customer', view=customer),
    path('carwasher/', name='carwasher', view=carwasher),
    path('create_order',view=create_order, name='create_order')
]
