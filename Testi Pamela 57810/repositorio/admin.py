from django.contrib import admin

# Register your models here.
from .models import *

class ProfesorAdmin (admin.ModelAdmin):
    list_filter = ("apellido",)

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Curso)
admin.site.register(AlumnoMateria)
admin.site.register(AlumnoProfesor)
admin.site.register(AlumnoCurso)
admin.site.register(CursoProfesor)
admin.site.register(CursoMateria)
admin.site.register(MateriaProfesor)