from .views import *
from django.urls import path

app_name = 'car_wash'

urlpatterns = [
    path('', name='home', view=home),
    path('order_list/', name='order_list', view=order_list),
    path('customers/', name='customer', view=customer),
    path('create_order',view=create_order, name='create_order'),
    path('washers/<int:pk>/', washer_detail, name='washer-detail'),
    path('update_order/<int:pk>', update_order, name='update_order'),
    path('delete/<int:pk>', delete_order, name='delete_order'),
    # path('search/', search, name='search')
]
