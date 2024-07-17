from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from repositorio.views import *
from . import views


urlpatterns = [
    path('', home, name="home"),
    path('materia/', materia, name="materia"),
    path('alumno/', alumno, name="alumno"),
    path('profesor/', profesor, name="profesor"),
    path('mundoliteriario/', mundoliterario, name="mundoliterario"),
    path('pdf/<str:pdf_file>/', pdf_viewer, name='pdf_viewer'),
    path('acerca/', acerca, name="acerca"),
    path('cursos/', curso, name='curso'),
    path('static/<path:file>', lambda x: serve(x, document_root=settings.STATIC_ROOT)),
    
    # Formularios
    path('alumnos/create/', alumno_create, name='alumno_create'),
    path('alumnos/', alumno_list, name='alumno_list'),
    path('profesores/create/', profesor_create, name='profesor_create'),
    path('profesores/', profesor_list, name='profesor_list'),
    path('cursos/create/', curso_create, name='curso_create'),
    path('cursos/', curso_list, name='curso_list'),
    path('materias/create/', materia_create, name='materia_create'),
    path('materias/', materia_list, name='materia_list'),
]