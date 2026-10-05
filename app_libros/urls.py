from django.urls import path
from app_libros import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
   
    path('', views.bienvenida, name='bienvenida_libros'),
    path('productos/', views.mostrar_libros, name='mostrar_libros'),
]
