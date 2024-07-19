from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.views import LogoutView
from repositorio.views import *
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('mundoliteriario/', mundoliterario, name="mundoliterario"),
    path('static/<path:file>', lambda x: serve(x, document_root=settings.STATIC_ROOT)),
    path('pdf/<str:pdf_file>/', pdf_viewer, name='pdf_viewer'),
    path('materia/', materia, name="materia"),
    path('profesor/', profesor, name="profesor"),
    path('alumno/', alumno, name="alumno"),
    path('curso/', curso, name="curso"),
    path('contacto/', contacto, name='contacto'),
    path('acerca/', acerca, name="acerca"),
    
#______________ Formularios
    path('alumnos/create/', alumno_create, name='alumno_create'),
    path('alumnoActualizar/<id_alumno>/', alumnoActualizar, name='alumnoActualizar'),
    path('alumnoEliminar/<id_alumno>/', alumnoEliminar, name='alumnoEliminar'),
   
    path('profesores/create/', profesor_create, name='profesor_create'),
    path('profActualizar/<id_profesor>/', profActualizar, name='profActualizar'),
    path('profEliminar/<id_profesor>/', profEliminar, name='profEliminar'),
    path('buscarProf/', buscarProf, name='buscarProf'),
    path('encontrarProf/', encontrarProf, name='encontrarProf'),
   
    path('cursos/create/', curso_create, name='curso_create'),
    path('cursosActualizar/<id_curso>/', cursosActualizar, name='cursosActualizar'),
    path('cursosEliminar/<id_curso>/', cursosEliminar, name='cursosEliminar'),
   
    path('materias/create/', materia_create, name='materia_create'),
    path('materiaActualizar/<id_materia>/', materiaActualizar, name='materiaActualizar'),
    path('materiaEliminar/<id_materia>/', materiaEliminar, name='materiaEliminar'),

#______________ Login, Logout, Registro
    path('login/', loginRequest, name='login'),
    path('logout/', LogoutView.as_view(template_name='repositorio/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),

#______________ Editar Perfil y Avatar
    path('perfil/', editarPerfil, name='perfil'),
    path('<int:pk>/password/', EditarClave.as_view() , name='editarClave'),
    path('addAvatar/', addAvatar, name='addAvatar'),
]



# ____________________________________ Código que fue reemplazado ____________________________________ 