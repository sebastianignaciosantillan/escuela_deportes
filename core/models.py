from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('administrador', 'Administrador'),
        ('supervisor', 'Supervisor'), #rol responsable
        ('empleado', 'Empleado'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def is_administrador(self):
        return self.role == 'administrador'

    def is_supervisor(self):
        return self.role == 'supervisor'
    
    def is_empleado(self):
        return self.role == 'empleado'


class Documento(models.Model):
    id_doc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    archivo = models.FileField(upload_to='documentos/')
    periodo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Escuela(models.Model):
    id_esc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    localidad = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=20, blank=True)
    telefono2 = models.CharField(max_length=20, blank=True)
    email = models.EmailField()

    documentos = models.ManyToManyField(Documento, related_name='escuelas')  # relación N:N

    def __str__(self):
        return self.nombre


class Responsable(models.Model):
    dni_reso = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=20, blank=True)
    telefono2 = models.CharField(max_length=20, blank=True)
    email = models.EmailField()

    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='responsables')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Entrenador(models.Model):
    dni_ent = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=255)
    telefono1 = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20)
    email = models.EmailField()

    escuela = models.ForeignKey(Escuela, on_delete=models.SET_NULL, null=True, related_name='entrenadores')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Capacitacion(models.Model):
    id_capacitacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=255)

    entrenadores = models.ManyToManyField(Entrenador, related_name='capacitaciones')

    def __str__(self):
        return self.nombre


class Disciplina(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    disciplina = models.CharField(max_length=100)

    entrenadores = models.ManyToManyField(Entrenador, related_name='disciplinas')  # Enseña
    escuelas = models.ManyToManyField(Escuela, related_name='disciplinas')  # Ofrece

    def __str__(self):
        return self.disciplina


class Alumno(models.Model):
    dni_alumno = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=255)
    fecha_nac = models.DateField()

    disciplinas = models.ManyToManyField(Disciplina, related_name='alumnos')  # Practica
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='alumnos')  # Inscribe

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Tutor(models.Model):
    dni_tutor = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=255)
    email = models.EmailField()

    alumnos = models.ManyToManyField(Alumno, related_name='tutores')  # Supervisa

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Empleado(models.Model):
    dni_emp = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=128)
    tipo = models.CharField(max_length=50)
    email = models.EmailField()
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, related_name='usuario')

    def __str__(self):
        return self.usuario


