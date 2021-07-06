from django.conf import settings
from django.db import models
from django.db.models.signals import m2m_changed

from productos.models import Producto

User = settings.AUTH_USER_MODEL

class CarritoManager(models.Manager):
    def new_or_get(self, request):
        carrito_id = request.session.get("carrito_id", None)
        qs = self.get_queryset().filter(id=carrito_id)
        if qs.count() == 1:
            nuevo_carrito = False
            carrito_obj = qs.first()
            if request.user.is_authenticated and carrito_obj.usuario is None:
                carrito_obj.usuario = request.user
                carrito_obj.save()
        else:
            carrito_obj = Carrito.objects.new(usuario=request.user)
            nuevo_carrito = True
            request.session['carrito_id'] = carrito_obj.id
        return carrito_obj, nuevo_carrito

    def new(self, usuario=None):
        user_obj = None
        if usuario is not None:
            if usuario.is_authenticated:
                user_obj = usuario
        return self.model.objects.create(usuario=user_obj)

class Carrito(models.Model):
    usuario         = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    productos       = models.ManyToManyField(Producto, blank=True)
    total           = models.DecimalField(default=0.00, max_digits=50, decimal_places=2)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects = CarritoManager()

    def __str__(self):
        return str(self.id)


def total_carrito(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        productos = instance.productos.all()
        total = 0
        for x in productos:
            total += x.precio
        instance.total = total
        instance.save()
m2m_changed.connect(total_carrito, sender=Carrito.productos.through)
