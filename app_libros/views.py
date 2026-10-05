from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro

def bienvenida(request):
    return HttpResponse("""
        <div style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>📚 Bienvenido a la Biblioteca</h1>
            <p>Sistema de gestión y control de libros.</p>
            <br>
            <a href="app_libros/libros/" style="padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px;">Ver Catálogo de Libros</a>
        </div>
    """)

def lista_libros(request):
    libros = Libro.objects.all()
    
    # Si la base de datos está vacía, usamos una lista de 10 libros de respaldo
    if not libros.exists():
        libros = [
            {'isbn': '978-0140449136', 'titulo': 'Cien años de soledad', 'descripcion': 'Historia de la familia Buendía en Macondo.', 'categoria': 'Realismo Mágico'},
            {'isbn': '978-8420653099', 'titulo': 'Don Quijote de la Mancha', 'descripcion': 'Aventuras de un hidalgo que enloquece leyendo.', 'categoria': 'Clásico'},
            {'isbn': '978-0307474728', 'titulo': '1984', 'descripcion': 'Novela distópica sobre el control social.', 'categoria': 'Ciencia Ficción'},
            {'isbn': '978-0451524935', 'titulo': 'Fahrenheit 451', 'descripcion': 'Sociedad donde los libros son quemados.', 'categoria': 'Ciencia Ficción'},
            {'isbn': '978-8437604947', 'titulo': 'Pedro Páramo', 'descripcion': 'Un hombre busca a su padre en un pueblo fantasma.', 'categoria': 'Realismo Mágico'},
            {'isbn': '978-0345806780', 'titulo': 'El Principito', 'descripcion': 'Un pequeño príncipe viaja descubriendo la naturaleza humana.', 'categoria': 'Fábula'},
            {'isbn': '978-8420682889', 'titulo': 'Crimen y Castigo', 'descripcion': 'Dilema moral de un estudiante tras un crimen.', 'categoria': 'Drama'},
            {'isbn': '978-8466332156', 'titulo': 'Orgullo y Prejuicio', 'descripcion': 'Choque entre Elizabeth Bennet y el Sr. Darcy.', 'categoria': 'Romance'},
            {'isbn': '978-0307743312', 'titulo': 'El resplandor', 'descripcion': 'Sucesos paranormales en un hotel aislado.', 'categoria': 'Terror'},
            {'isbn': '978-8420633114', 'titulo': 'La odisea', 'descripcion': 'El viaje de regreso a casa del héroe Odiseo.', 'categoria': 'Épico'}
        ]

    contexto = {'libros': libros}
    return render(request, 'App_Libros/libros.html', contexto)

def mostrar_libros(request):
    return lista_libros(request)