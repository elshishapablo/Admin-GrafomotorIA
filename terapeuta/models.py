from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    tipo_usuario = models.CharField(
        max_length=50,
        choices=(
            ('terapeuta', 'Terapeuta'),
            ('otro', 'Otro'),
        ),
        default='terapeuta'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(_('Correo electrónico'), unique=True)

    # Evitamos choques de related_name con Django
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='usuario_groups',
        related_query_name='usuario',
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='usuario_user_permissions',
        related_query_name='usuario_permission',
        help_text=_('Specific permissions for this user.'),
    )

    def __str__(self):
        return f"{self.username} ({self.email})"

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuario'


class Tutor(models.Model):
    nombre           = models.CharField(max_length=80)
    apellido         = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    rut              = models.CharField(max_length=12, unique=True)
    numero_telefono  = models.CharField(max_length=20)
    correo           = models.EmailField(max_length=150, unique=True)
    direccion        = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'tutor'
        verbose_name_plural = 'tutor'


class Paciente(models.Model):
    nombre              = models.CharField(max_length=80)
    apellido            = models.CharField(max_length=80)
    fecha_nacimiento    = models.DateField()
    rut                 = models.CharField(max_length=12, unique=True)
    diagnostico         = models.CharField(max_length=50)
    alergias            = models.CharField(max_length=50, blank=True)
    medicamentos        = models.CharField(max_length=50, blank=True)
    nombre_emergencia   = models.CharField(max_length=80)
    contacto_emergencia = models.CharField(max_length=20)
    correo              = models.EmailField(max_length=80, unique=True)
    nivel_autonomia     = models.CharField(max_length=50)
    indice_barthel      = models.IntegerField()
    tutor               = models.ForeignKey(Tutor, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'paciente'


class PlanTratamiento(models.Model):
    paciente       = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    usuario        = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha_inicio   = models.DateField()
    fecha_fin      = models.DateField()
    objetivo_corto = models.TextField()
    objetivo_largo = models.TextField()
    periodicidad   = models.CharField(max_length=25)

    def __str__(self):
        return f"Plan {self.id} - {self.paciente}"

    class Meta:
        verbose_name = 'plan_tratamiento'
        verbose_name_plural = 'plan_tratamiento'


class Sesion(models.Model):
    paciente      = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    usuario       = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha_sesion  = models.DateTimeField()
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Sesión {self.id} - {self.paciente}"

    class Meta:
        verbose_name = 'sesion'
        verbose_name_plural = 'sesion'


class Ejercicio(models.Model):
    nombre_ejercicio  = models.CharField(max_length=255, unique=True)
    descripcion       = models.TextField()
    imagen_ejercicio  = models.BinaryField(blank=True, null=True)
    tipo_ejercicio    = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_ejercicio

    class Meta:
        verbose_name = 'ejercicio'
        verbose_name_plural = 'ejercicio'


class DetalleSesion(models.Model):
    sesion    = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.SET_NULL, null=True)
    resultado = models.TextField(blank=True)
    puntaje   = models.IntegerField()

    def __str__(self):
        return f"Detalle {self.id} de Sesión {self.sesion.id}"

    class Meta:
        verbose_name = 'detalle_sesion'
        verbose_name_plural = 'detalle_sesion'


class EvaluacionEscala(models.Model):
    paciente    = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha       = models.DateField()
    tipo_escala = models.CharField(max_length=100)
    resultado   = models.CharField(max_length=100)
    puntaje     = models.IntegerField()

    def __str__(self):
        return f"{self.tipo_escala} ({self.paciente})"

    class Meta:
        verbose_name = 'evaluacion_escala'
        verbose_name_plural = 'evaluacion_escala'


class SeguimientoProgreso(models.Model):
    paciente     = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha        = models.DateField()
    observaciones= models.TextField()
    nivel_logro  = models.IntegerField()
    comentarios  = models.TextField(blank=True)

    def __str__(self):
        return f"Seguimiento {self.id} - {self.paciente}"

    class Meta:
        verbose_name = 'seguimiento_progreso'
        verbose_name_plural = 'seguimiento_progreso'


# ¨¨¨¨¨¨ Tablas MYsql ¨¨¨¨¨¨
"""""
class Autonomia(models.Model):
    nivel_autonomia = models.CharField(max_length=20)
    indice_barthel = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'autonomia'

    def __str__(self):
        return self.nivel_autonomia

class AsignacionEjercicio(models.Model):
    instrucciones = models.CharField(max_length=100)
    id_plan = models.ForeignKey('PlanTratamiento', on_delete=models.CASCADE)
    id_ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'asignacion_ejercicio'

class Tutor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    rut = models.CharField(unique=True, max_length=12)
    numero_telefono = models.CharField(max_length=12)
    correo = models.CharField(max_length=150)
    direccion = models.CharField(max_length=100)

    class Meta:
        db_table = 'tutor'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    rut = models.CharField(unique=True, max_length=12)
    diagnostico = models.CharField(max_length=50)
    alergias = models.CharField(max_length=50, blank=True, null=True)
    medicamentos = models.CharField(max_length=50, blank=True, null=True)
    nombre_emergencia = models.CharField(max_length=80)
    contacto_emergencia = models.CharField(max_length=12)
    correo = models.CharField(max_length=80, blank=True, null=True)
    id_autonomia = models.ForeignKey(Autonomia, on_delete=models.CASCADE)
    id_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class TipoEjercicio(models.Model):
    nombre_ejercicio = models.CharField(max_length=500)

    class Meta:
        db_table = 'tipo_ejercicio'


class Ejercicio(models.Model):
    nombre_ejercicio = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    imagen_ejercicio = models.TextField(blank=True, null=True)
    id_tipo_ejercicio = models.ForeignKey(TipoEjercicio, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ejercicio'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)  # 👈 esto reemplaza a id por defecto
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=80)
    contrasena = models.CharField(max_length=45)

    class Meta:
        db_table = 'usuario'



class Sesion(models.Model):
    fecha_sesion = models.DateTimeField()
    observaciones = models.CharField(max_length=1000, blank=True, null=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sesion'

class PlanTratamiento(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    objetivo_cortoplazo = models.CharField(max_length=100)
    objetivo_largoplazo = models.CharField(max_length=100)
    periodicidad = models.CharField(max_length=50)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'plan_tratamiento'


class EvaluacionEscala(models.Model):
    fecha = models.DateField()
    tipo_escala = models.CharField(max_length=100)
    resultado = models.CharField(max_length=100)
    puntaje = models.IntegerField()
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)

    class Meta:
        db_table = 'evaluacion_escala'


class Reporte(models.Model):
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    fecha_generacion = models.DateField()
    contenido = models.CharField(max_length=100)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    tipo_reporte = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'reporte'


class SeguimientoProgreso(models.Model):
    fecha = models.DateField()
    observaciones = models.CharField(max_length=1000)
    nivel_logro = models.IntegerField()
    comentarios = models.CharField(max_length=100, blank=True, null=True)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)

    class Meta:
        db_table = 'seguimiento_progreso'


class TipoUsuario(models.Model):
    nombre_tipo_usuario = models.CharField(max_length=500)

    class Meta:
        db_table = 'tipo_usuario'

class DetalleSesion(models.Model):
    resultado = models.CharField(max_length=1000)
    comentarios = models.CharField(max_length=500, blank=True, null=True)
    puntaje = models.IntegerField()
    id_sesion = models.ForeignKey('Sesion', on_delete=models.CASCADE)
    id_ejercicio = models.ForeignKey('Ejercicio', on_delete=models.CASCADE)

    class Meta:
        db_table = 'detalle_sesion'

"""