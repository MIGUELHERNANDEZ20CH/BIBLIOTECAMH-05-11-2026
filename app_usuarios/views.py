from django.http import HttpResponse

def registro_usuario(request):
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Registro de Usuario</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container my-5">
            <div class="row g-4">
                <div class="col-md-5">
                    <div class="card border-0 shadow-sm h-100">
                        <div class="card-header bg-dark text-white fw-bold">📋 Reglas de la Biblioteca</div>
                        <div class="card-body">
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">1. Mantener silencio en la sala.</li>
                                <li class="list-group-item">2. Cuidar los libros prestados.</li>
                                <li class="list-group-item">3. Devolver los libros a tiempo.</li>
                                <li class="list-group-item">4. No consumir alimentos ni bebidas.</li>
                                <li class="list-group-item">5. Presentar carné para préstamos.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-md-7">
                    <div class="card border-0 shadow-sm">
                        <div class="card-header bg-primary text-white fw-bold">📝 Formulario de Registro</div>
                        <div class="card-body p-4">
                            <form>
                                <div class="mb-3"><label class="form-label">Nombre Completo</label><input type="text" class="form-control" required></div>
                                <div class="mb-3"><label class="form-label">Correo Electrónico</label><input type="email" class="form-control" required></div>
                                <div class="mb-3"><label class="form-label">Documento de Identidad</label><input type="text" class="form-control" required></div>
                                <div class="mb-3"><label class="form-label">Teléfono</label><input type="tel" class="form-control" required></div>
                                <button type="submit" class="btn btn-primary w-100">Registrarse</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <div class="mt-4 text-center"><a href="/" class="btn btn-link text-decoration-none">← Volver al Inicio</a></div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)