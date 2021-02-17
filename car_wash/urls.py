from django.contrib.auth.decorators import login_required as lr

from .views import *
from django.urls import path
app_name = 'car_wash'

urlpatterns = [
    path('', view=home, name='home'),
    path('order_list/', view=order_list, name='order_list'),
    path('customers/', view=customer, name='customer'),
    path('create_order/', view=create_order, name='create_order'),
    path('washer_detail/<int:pk>/', view=washer_detail, name='washer-detail'),
    path('update_order/<int:pk>', view=update_order, name='update_order'),
    path('delete/<int:pk>', view=delete_order, name='delete_order'),
    path('contact/', view=contact, name='contact'),
    path('about/', view=about, name='about'),
    path('add_car/', view=add_car, name='add_car'),
    path('cars/', view=cars_list, name='cars_list'),
    path('washers/', view=washers_list, name='washers_list'),
]
