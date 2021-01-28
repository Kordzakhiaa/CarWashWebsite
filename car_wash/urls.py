from .views import Home
from django.urls import path

urlpatterns = [
    path('home/', view=Home)
]
