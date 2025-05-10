from django.contrib import admin
from .models import (
    AsignacionEjercicio,
    Autonomia,
    DetalleSesion,
    Ejercicio,
    EvaluacionEscala,
    Paciente,
    PlanTratamiento,
    Reporte,
    SeguimientoProgreso,
    Sesion,
    TipoEjercicio,
    TipoUsuario,
    Tutor,
    Usuario
)

modelos = [
    AsignacionEjercicio,
    Autonomia,
    DetalleSesion,
    Ejercicio,
    EvaluacionEscala,
    Paciente,
    PlanTratamiento,
    Reporte,
    SeguimientoProgreso,
    Sesion,
    TipoEjercicio,
    TipoUsuario,
    Tutor,
    Usuario
]

for modelo in modelos:
    admin.site.register(modelo)
