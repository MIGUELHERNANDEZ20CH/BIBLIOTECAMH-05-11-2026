from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Bienvenido a la Biblioteca</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm">
            <div class="container">
                <a class="navbar-brand fw-bold" href="/">📚 Biblioteca Central</a>
                <div>
                    <a class="btn btn-outline-light me-2" href="/app_usuarios/registro/">Registro</a>
                    <a class="btn btn-warning" href="/app_libros/libros/">Libros</a>
                </div>
            </div>
        </nav>
        <div class="container py-5 text-center">
            <div class="p-5 mb-4 bg-white rounded-3 shadow-sm border">
                <h1 class="display-4 fw-bold text-primary">¡Bienvenido a la Biblioteca!</h1>
                <p class="lead mt-3 text-secondary">Página web de bienvenida a la biblioteca. Tu espacio ideal para la lectura y la investigación.</p>
                <hr class="my-4">
                <div class="d-flex justify-content-center gap-3">
                    <a href="/app_libros/libros/" class="btn btn-primary btn-lg">Ver Catálogo</a>
                    <a href="/app_usuarios/registro/" class="btn btn-outline-secondary btn-lg">Registro de Usuarios</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)