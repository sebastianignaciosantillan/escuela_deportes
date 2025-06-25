from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Alumno,
    Capacitacion,
    CustomUser,
    Disciplina,
    Documento,
    Empleado,
    Entrenador,
    Escuela,
    Responsable,
    Tutor,
    Usuario,
)

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id_doc', 'nombre', 'tipo', 'periodo')
    search_fields = ('nombre', 'tipo')
    list_filter = ('tipo', 'periodo')


@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('id_esc', 'nombre', 'localidad', 'email')
    search_fields = ('nombre', 'localidad')
    list_filter = ('localidad',)


@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('dni_reso', 'nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'dni_reso')


@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ('dni_ent', 'nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'dni_ent')
    list_filter = ('escuela',)


@admin.register(Capacitacion)
class CapacitacionAdmin(admin.ModelAdmin):
    list_display = ('id_capacitacion', 'nombre', 'estado', 'fecha', 'ubicacion')
    search_fields = ('nombre', 'estado')
    list_filter = ('estado', 'fecha')


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('id_disciplina', 'disciplina',)
    search_fields = ('disciplina',)


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('dni_alumno', 'nombre', 'apellido', 'fecha_nac')
    search_fields = ('nombre', 'apellido', 'dni_alumno')
    list_filter = ('escuela', 'disciplinas')


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('dni_tutor', 'nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'dni_tutor')


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('dni_emp', 'nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'dni_emp')


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'email')
    search_fields = ('usuario', 'tipo', 'email')


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']
    search_fields = ['username', 'email', 'role']
    ordering = ['username']

    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('role',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
