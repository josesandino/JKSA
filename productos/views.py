from django.shortcuts import get_object_or_404, render
from django.db import models
from django.db.models import Q
from django.views.generic.list import ListView

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



