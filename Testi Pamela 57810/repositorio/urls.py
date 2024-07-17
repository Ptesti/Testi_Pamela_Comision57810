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
    path('cursos/', CursoList.as_view(), name='curso'),
    path('static/<path:file>', lambda x: serve(x, document_root=settings.STATIC_ROOT)),
    
    # Formularios
    path('alumnos/create/', alumno_create, name='alumno_create'),
    path('alumnos/', alumno_list, name='alumno_list'),
    path('alumnoActualizar/<id_alumno>/', alumnoActualizar, name='alumnoActualizar'),
    path('alumnoEliminar/<id_alumno>/', alumnoEliminar, name='alumnoEliminar'),
   
    path('profesores/create/', profesor_create, name='profesor_create'),
    path('profesores/', profesor_list, name='profesor_list'),
    path('profActualizar/<id_profesor>/', profActualizar, name='profActualizar'),
    path('profEliminar/<id_profesor>/', profEliminar, name='profEliminar'),
    path('buscarProf/', buscarProf, name='buscarProf'),
    path('encontrarProf/', encontrarProf, name='encontrarProf'),
   
    path('cursosCreate/', CursoCreate.as_view(), name='cursoCreate'),
    path('cursos/', curso_list, name='curso_list'),
    path('cursosActualizar/<id_curso>/', cursosActualizar, name='cursosActualizar'),
    path('cursosEliminar/<id_curso>/', cursosEliminar, name='cursosEliminar'),
   
    path('materias/create/', materia_create, name='materia_create'),
    path('materias/', materia_list, name='materia_list'),
    path('materiaActualizar/<id_materia>/', materiaActualizar, name='materiaActualizar'),
    path('materiaEliminar/<id_materia>/', materiaEliminar, name='materiaEliminar'),
]

# ____________________________________ Código que fue reemplazado ____________________________________ 
#    path('curso/', curso, name="curso"),