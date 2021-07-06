
from django.urls import path
from . import views


app_name = "carritos"
urlpatterns = [
    path('', views.carrito, name="compra"),
    path('update/', views.carrito_actualizado, name='update'),
    path('borrar_carrito/<int:carrito_id>', views.carrito_borrado, name="carrito_borrado"),

]