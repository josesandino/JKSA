from django.urls import path
from . import views

from .views import SearchResultsView

app_name = "productos"
urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('acerca/', views.acerca, name="acerca"),
    path('resultado/', SearchResultsView.as_view(), name="resultado"),
    path('producto/<int:producto_id>', views.producto, name="producto"),
    path('producto_nuevo', views.crear_producto, name="producto_nuevo"),
    path('editar_producto/<int:producto_id>', views.editar_producto, name="editar_producto"),
    path('borrar_producto/<int:producto_id>', views.producto_borrado, name="producto_borrado"),

]