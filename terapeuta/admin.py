# terapeuta/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Usuario

from .models import (
    Usuario,
    Tutor,
    Paciente,
    PlanTratamiento,
    Sesion,
    Ejercicio,
    DetalleSesion,
    EvaluacionEscala,
    SeguimientoProgreso,
)

@admin.register(Usuario)
class UsuarioAdmin(DjangoUserAdmin):
    model = Usuario

    # Columnas que mostrarán en el changelist
    list_display = (
        'username',      # nombre de usuario
        'email',         # correo (campo email)
        'tipo_usuario',  # tu campo extra
        'is_staff',
        'is_active',
    )
    list_filter = ('tipo_usuario', 'is_staff', 'is_active')

    # Usa los fieldsets de DjangoUserAdmin para username/email/password
    fieldsets = DjangoUserAdmin.fieldsets + (
        (None, {'fields': ('tipo_usuario',)}),
    )

    # Opcionalmente, en el formulario de creación
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        (None, {'fields': ('tipo_usuario',)}),
    )

    search_fields = ('username', 'email')
    ordering = ('email',)


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'apellido', 'rut', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido', 'rut')


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'apellido', 'rut', 'diagnostico', 'tutor')
    list_filter   = ('diagnostico', 'tutor')
    search_fields = ('nombre', 'apellido', 'rut')


@admin.register(PlanTratamiento)
class PlanTratamientoAdmin(admin.ModelAdmin):
    list_display    = ('id', 'paciente', 'usuario', 'fecha_inicio', 'fecha_fin')
    list_filter     = ('usuario',)
    date_hierarchy  = 'fecha_inicio'
    search_fields   = ('paciente__nombre', 'usuario__username')


@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display    = ('id', 'paciente', 'usuario', 'fecha_sesion')
    list_filter     = ('usuario',)
    date_hierarchy  = 'fecha_sesion'
    search_fields   = ('paciente__nombre', 'usuario__username')


@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display    = ('nombre_ejercicio', 'tipo_ejercicio')
    search_fields   = ('nombre_ejercicio', 'tipo_ejercicio')


@admin.register(DetalleSesion)
class DetalleSesionAdmin(admin.ModelAdmin):
    list_display  = ('id', 'sesion', 'ejercicio', 'puntaje')
    list_filter   = ('ejercicio',)
    search_fields = ('sesion__paciente__nombre', 'ejercicio__nombre_ejercicio')


@admin.register(EvaluacionEscala)
class EvaluacionEscalaAdmin(admin.ModelAdmin):
    list_display  = ('id', 'paciente', 'tipo_escala', 'puntaje', 'fecha')
    list_filter   = ('tipo_escala',)
    date_hierarchy = 'fecha'
    search_fields = ('paciente__nombre', 'tipo_escala')


@admin.register(SeguimientoProgreso)
class SeguimientoProgresoAdmin(admin.ModelAdmin):
    list_display  = ('id', 'paciente', 'fecha', 'nivel_logro')
    date_hierarchy = 'fecha'
    search_fields = ('paciente__nombre',)