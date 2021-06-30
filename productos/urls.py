from django.urls import path
from . import views

from .views import SearchResultsView


app_name = "productos"
urlpatterns = [
    path('', views.home, name="home"),
    path('acerca/', views.acerca, name="acerca"),
    path('resultado/', SearchResultsView.as_view(), name="resultado"),
]