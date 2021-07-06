from django.shortcuts import render, redirect

from productos.models import Producto
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

def carrito_actualizado(request):
    producto_id = 2
    item = Producto.objects.get(id=producto_id)
    carrito_obj, nuevo_carrito = Carrito.objects.new_or_get(request)
    if item in carrito_obj.productos.all():
        carrito_obj.productos.remove(item)
    else:
        carrito_obj.productos.add(item)
    return redirect('carritos:compra')