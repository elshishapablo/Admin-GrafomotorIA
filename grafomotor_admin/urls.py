from django.contrib import admin
from django.urls import path
from pacientes.views import lista_usuarios
from pacientes.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # ← ahora la raíz es el login
    path('usuarios/', lista_usuarios, name='usuarios'),
]

