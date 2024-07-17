from django.contrib import admin

# Register your models here.
from .models import *

class ProfesorAdmin (admin.ModelAdmin):
    list_filter = ("apellido",)

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Curso)