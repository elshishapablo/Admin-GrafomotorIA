from django.shortcuts import render, redirect
from .models import Usuario

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'pacientes/usuarios.html', {'usuarios': usuarios})


def login_view(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        if 'usuario_id' in request.session:
            return redirect('usuarios')  # Ya ha iniciado sesión
        try:
            usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
            request.session['usuario_id'] = usuario.id_usuario
            return redirect('usuarios')  # o a la vista que quieras después del login
        except Usuario.DoesNotExist:
            return render(request, 'pacientes/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'pacientes/login.html')
