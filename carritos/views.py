from django.shortcuts import render

from .models import Carrito

def carrito(request):
    carrito_obj, nuevo_carrito = Carrito.objects.new_or_get(request)
    productos = carrito_obj.productos.all()
    total = 0
    for x in productos:
        total += x.precio
    print(total)
    carrito_obj.total = total
    carrito_obj.save()
    return render(request, "carrito/carrito.html", {})