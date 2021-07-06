from django.shortcuts import render

from .models import Carrito

def carrito(request):
    carrito_obj = Carrito.objects.new_or_get(request)
    return render(request, "carrito/carrito.html", {})