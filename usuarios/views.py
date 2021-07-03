from usuarios.forms import RegistroForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from productos.models import Categoria

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        categorias = Categoria.objects.all()
        form = RegistroForm()
    return render(request, 'registration/register.html', {
        'form': form,
        'categorias': categorias,
        })
