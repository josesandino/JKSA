
from django.urls import path
from . import views


app_name = "carritos"
urlpatterns = [
    path('', views.carrito, name="carrito"),
]