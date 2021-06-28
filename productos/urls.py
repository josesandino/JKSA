from django.urls import path
from . import views


app_name = "productos"
urlpatterns = [
    path('', views.home, name="home"),
]