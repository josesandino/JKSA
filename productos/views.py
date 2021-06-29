from django.shortcuts import render

from .models import Categoria, Producto

# Create your views here.
def home(request):
    productos13 = Producto.objects.all()[:3]
    productos410 = Producto.objects.all()[3:10]
    categorias = Categoria.objects.all()
    context = {
        'primeros_productos': productos13,
        'segundos_productos': productos410,
        'lista_categorias': categorias,
    }
    return render(request, "home.html", context)