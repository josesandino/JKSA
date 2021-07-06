from django.shortcuts import get_object_or_404, render, redirect

from productos.models import Producto, Categoria
from .models import Carrito

def carrito(request):
    categorias = Categoria.objects.all()
    carrito_obj, nuevo_carrito = Carrito.objects.new_or_get(request)
    context = {
        'carrito': carrito_obj,
        'categorias': categorias,
    }
    return render(request, "carrito/carrito.html", context)

def carrito_actualizado(request):
    producto_id = request.POST.get('producto_id')
    if producto_id is not None:
        item = Producto.objects.get(id=producto_id)
        carrito_obj, nuevo_carrito = Carrito.objects.new_or_get(request)
        if item in carrito_obj.productos.all():
            carrito_obj.productos.remove(item)
        else:
            carrito_obj.productos.add(item)
    return redirect('carritos:compra')


def carrito_borrado(request, carrito_id):
    borrado = get_object_or_404(Carrito, id=carrito_id)
    borrado.delete()
    return redirect("carritos:compra")
