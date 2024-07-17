from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.conf import settings
from django.http import FileResponse
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from repositorio.models import *
from .forms import * 
import os #para obtener una lista de archivos en la carpeta, en este caso 'static/pdf'

# Create your views here.
def home(request):
    return render(request, "repositorio/index.html")

def alumno(request):
    context = {"alumnos": Alumno.objects.all()}
    return render(request, "repositorio/alumno.html", context)

def profesor(request):
    context = {"profesores": Profesor.objects.all()}
    return render(request, "repositorio/profesor.html", context)

def materia(request):
    context = {"materias": Materia.objects.all()}
    return render(request, "repositorio/materia.html", context)

def mundoliterario(request):
    return render(request, "repositorio/MundoLiterario.html")

def mundoliterario(request):
    pdf_files = os.listdir('repositorio/static/pdf') 
    return render(request, 'repositorio/MundoLiterario.html', {'pdf_files': pdf_files})

def pdf_viewer(request, pdf_file):
    file_path = os.path.join(settings.STATIC_ROOT, 'pdf', pdf_file)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponse("File not found.", status=404)

def acerca(request):
    return render(request, "repositorio/acerca.html")

class CursoList (ListView):
    model = Curso

# Formularios

def alumno_create(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm()
    return render(request, 'repositorio/alumno_form.html', {'form': form})

def alumno_list(request):
    alumnos = Alumno.objects.all()
    return render(request, 'repositorio/alumno_list.html', {'alumnos': alumnos})

def alumnoActualizar (request,id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    if request.method == 'POST': 
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm(initial={"nombre": alumno.nombre,
                                   "apellido": alumno.apellido,})

    return render(request, 'repositorio/alumno_form.html', {'form': form})

def alumnoEliminar (request,id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    alumno.delete()
    contexto = {"alumno": Alumno.objects.all()}
    return render(request, "repositorio/alumno.html", contexto)

def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm()
    return render(request, 'repositorio/profesor_form.html', {'form': form})

def profesor_list(request):
    profesores = Profesor.objects.all()
    return render(request, 'repositorio/profesor_list.html', {'profesores': profesores})

def profActualizar (request,id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == 'POST': 
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm(initial={"nombre": profesor.nombre,
                                     "apellido": profesor.apellido,
                                     "email": profesor.email})

    return render(request, 'repositorio/profesor_form.html', {'form': form})

def profEliminar (request,id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "repositorio/profesor.html", contexto)

class CursoCreate (CreateView):
    model = Curso
    fields = ["nombre", "division", "turno"] 
    success_url = reverse_lazy ("curso")

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'repositorio/curso_list.html', {'cursos': cursos})

def cursosActualizar (request,id_curso):
    curso = Curso.objects.get(id=id_curso)
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm(initial={
            "nombre": curso.nombre,
            "division": curso.division,
            "turno": curso.get_turno_display()
            })
        
    return render(request, 'repositorio/curso_form.html', {'form': form})

def cursosEliminar (request,id_curso):
    curso = Curso.objects.get(id=id_curso)
    curso.delete()
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "repositorio/curso.html", contexto)

def materia_create(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materia_list')
    else:
        form = MateriaForm()
    return render(request, 'repositorio/materia_form.html', {'form': form})

def materia_list(request):
    materias = Materia.objects.all()
    return render(request, 'repositorio/materia_list.html', {'materias': materias})

def materiaActualizar (request,id_materia):
    materia = Materia.objects.get(id=id_materia)
    if request.method == "POST":
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materia_list')
    else:
        form = MateriaForm(initial={
            "nombre": materia.nombre,
            "codigo": materia.codigo,
            })
        
    return render(request, 'repositorio/materia_form.html', {'form': form})

def materiaEliminar (request,id_materia):
    materia = Materia.objects.get(id=id_materia)
    materia.delete()
    contexto = {"materias": Materia.objects.all()}
    return render(request, "repositorio/materia.html", contexto)

# Buscar
def buscarProf (request):
    return render (request, "repositorio/buscar.html")

def encontrarProf (request):
    if request.GET ["buscar"]:
        dato = request.GET ["buscar"]
        prof = Profesor.objects.filter(nombre__icontains=dato)
        contexto = {"profesores": prof}
    else:
        contexto = {"profesores": Profesor.objects.all()}
    
    return render (request, "repositorio/profesor.html", contexto)


# ____________________________________ Código que fue reemplazado ____________________________________ 
# def curso(request):
#    cursos = Curso.objects.all()
#    contexto = {"cursos": cursos}
#    return render(request, "repositorio/curso.html", contexto)

# def curso_create(request):
#    if request.method == 'POST':
#        form = CursoForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('curso_list')
#    else:
#        form = CursoForm()
#    return render(request, 'repositorio/curso_form.html', {'form': form})