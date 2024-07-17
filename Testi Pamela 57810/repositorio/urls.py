from django.urls import path, include
from repositorio.views import *
from . import views
 
urlpatterns = [
    path('', home, name="home"),
    path('materia/', materia, name="materia"),
    path('alumno/', alumno, name="alumno"),
    path('profesor/', profesor, name="profesor"),
    path('mundoliteriario/', mundoliterario, name="mundoliterario"),
    path('acerca/', acerca, name="acerca"),
    
    # Formularios

    path('alumnos/create/', alumno_create, name='alumno_create'),
    path('profesor/create/', profesor_create, name='profesor_create'),
    path('profesor/', profesor_list, name='profesor_list'),
    path('cursos/create/', curso_create, name='curso_create'),
    path('materia/create/', materia_create, name='materia_create'),
    path('profesor/', materia_list, name='materia_list'),
]