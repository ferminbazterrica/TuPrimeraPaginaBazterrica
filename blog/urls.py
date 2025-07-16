from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nuevo-autor/', views.crear_autor, name='nuevo_autor'),
    path('nueva-categoria/', views.crear_categoria, name='nueva_categoria'),
    path('nuevo-post/', views.crear_post, name='nuevo_post'),
    path('buscar-post/', views.buscar_post, name='buscar_post'),
]