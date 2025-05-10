from django.contrib import admin
from django.urls import path
from terapeuta.views import lista_usuarios
from terapeuta.views import login_view


urlpatterns = [
#    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # ← ahora la raíz es el login
    path('usuarios/', lista_usuarios, name='usuarios'),
]

