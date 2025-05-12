from django.shortcuts import render, redirect
from .models import Usuario, Paciente
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required  

def login_view(request):
    error = None
    if request.method == 'POST':
        correo    = request.POST.get('correo')
        contrasena= request.POST.get('contrasena')
        user = authenticate(request, username=correo, password=contrasena)
        if user is not None:
            login(request, user)
            return redirect('listaTerapeuta')
        else:
            error = "Credenciales inválidas."
    return render(request, 'terapeuta/login.html', {'error': error})

@login_required(login_url='login')  # <-- protege la vista, y si no está autenticado redirige a 'login'
def listaTerapeuta_view(request):
    terapeutas = Usuario.objects.filter(tipo_usuario='terapeuta')
    return render(request,
                  'terapeuta/listaTerapeuta.html',
                  {'terapeutas': terapeutas})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'terapeuta/usuarios.html', {
        'usuarios': usuarios
    })

def listaTerapeuta_view(request):
    # Filtramos sólo a los usuarios cuyo tipo sea "terapeuta"
    terapeutas = Usuario.objects.filter(tipo_usuario='terapeuta')
    return render(request, 'terapeuta/listaTerapeuta.html', {
        'terapeutas': terapeutas
    })
