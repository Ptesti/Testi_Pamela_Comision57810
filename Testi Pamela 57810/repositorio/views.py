from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.conf import settings
from repositorio.models import *
from .forms import * 
import os #para obtener una lista de archivos en la carpeta, en este caso 'static/pdf'
from django.http import FileResponse

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

def acerca(request):
    return render(request, "repositorio/acerca.html")

def curso(request):
    cursos = Curso.objects.all()
    context = {"cursos": cursos}
    return render(request, "repositorio/curso.html", context)

def mundoliterario(request):
    pdf_files = os.listdir('repositorio/static/pdf') 
    return render(request, 'repositorio/MundoLiterario.html', {'pdf_files': pdf_files})

def pdf_viewer(request, pdf_file):
    file_path = os.path.join(settings.STATIC_ROOT, 'pdf', pdf_file)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponse("File not found.", status=404)
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

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'repositorio/curso_form.html', {'form': form})

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'repositorio/curso_list.html', {'cursos': cursos})

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
