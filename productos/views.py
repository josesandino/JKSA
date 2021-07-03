from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db import models
from .forms import *
from django.db.models import Q
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Categoria, Producto

def home(request):
    productos13 = Producto.objects.all()[:3]
    productos410 = Producto.objects.all()[3:10]
    categorias = Categoria.objects.all()
    context = {
        'primeros_productos': productos13,
        'segundos_productos': productos410,
        'categorias': categorias,
    }
    return render(request, "home.html", context)

def acerca(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, "acerca.html", context)

def resultado(request, categoria_id):
    categoria_id = get_object_or_404(Categoria, id=categoria_id)
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'id_cat': categoria_id,
    }
    return render(request, "search/resultado.html", context)

def producto(request, producto_id):
    categorias = Categoria.objects.all()
    un_producto =get_object_or_404(Producto, id=producto_id)
    context = {
        'producto': un_producto,
        'categorias': categorias,
    }
    return render(request, "product/producto.html", context)

def crear_producto(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = FormProducto(request.POST, request.FILES, 
            initial={'fecha':timezone.now()}, 
            instance=Producto(imagen=request.FILES['imagen'], 
            moderador=user,            
            ))
        if form.is_valid():
            form.save()
            return redirect("productos:home")
    else:
        form = FormProducto(initial={'fecha':timezone.now()})
        categorias = Categoria.objects.all()
        return render(request, "product/producto_nuevo.html", {
            'categorias': categorias,
            "form": form
        })

def editar_producto(request, producto_id):
    producto_editado = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        producto_editado.moderador = user
        form = FormProducto(data=request.POST, files=request.FILES, instance=producto_editado)
        if form.is_valid():
            form.save()
            return redirect("productos:home")
    else:
        form = FormProducto(instance = producto_editado)
        categorias = Categoria.objects.all()
        context = {
            'categorias': categorias,
            "producto": producto_editado,
            "form": form
        }
        return render(request, 'product/producto_editado.html', context)

def categorias(request, categoria_id):
    categoria_id = get_object_or_404(Categoria, id=categoria_id)
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'id_cat': categoria_id,
    }
    return render(request, "base/navbar.html", context)

class SearchResultsView(ListView):
    model = Producto
    template_name = 'search/resultado.html'
        
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Producto.objects.filter(
             Q(titulo__icontains=query) | 
             Q(descripcion__icontains=query)
        )
        return object_list 



