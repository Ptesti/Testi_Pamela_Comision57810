from django.shortcuts import render, redirect
from django.template import Template, Context
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.conf import settings
from django.http import FileResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin #trabajan sobre las clases
from django.contrib.auth.decorators import login_required #trabajan sobre las funciones
from repositorio.models import *
from .forms import * 
import os #para obtener una lista de archivos en la carpeta, en este caso 'static/pdf'
from django.contrib import messages


#______________ index

def home(request):
    return render(request, "repositorio/index.html")

#______________ Mundo Literario

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

#______________ Materia

@login_required
def materia(request):
    context = {"materias": Materia.objects.all()}
    return render(request, "repositorio/materia.html", context)

# Formularios Materia

@login_required
def materia_create(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materia')
    else:
        form = MateriaForm()
    return render(request, 'repositorio/materia_form.html', {'form': form})

@login_required
def materiaActualizar (request,id_materia):
    materia = Materia.objects.get(id=id_materia)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('materia')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'repositorio/materia_form.html', {'form': form})

@login_required
def materiaEliminar (request,id_materia):
    materia = Materia.objects.get(id=id_materia)
    materia.delete()
    return redirect('materia')

#______________ Profesor

@login_required
def profesor(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "repositorio/profesor.html", contexto)

# Formularios Profesor

@login_required
def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor')
    else:
        form = ProfesorForm()
    return render(request, 'repositorio/profesor_form.html', {'form': form})

@login_required
def profActualizar (request,id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('profesor')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'repositorio/profesor_form.html', {'form': form})

@login_required
def profEliminar (request,id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    return redirect('profesor')

#______________ Buscar

@login_required
def buscarProf (request):
    return render (request, "repositorio/buscar.html")

@login_required
def encontrarProf (request):
    if request.GET ["buscar"]:
        dato = request.GET ["buscar"]
        prof = Profesor.objects.filter(nombre__icontains=dato)
        contexto = {"profesores": prof}
    else:
        contexto = {"profesores": Profesor.objects.all()}
    
    return render (request, "repositorio/profesor.html", contexto)

#______________ alumno

@login_required
def alumno(request):
    contexto = {"alumnos": Alumno.objects.all()}
    return render(request, "repositorio/alumno.html", contexto)

# Formularios Alumno

@login_required
def alumno_create(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno')
        
    else:
        form = AlumnoForm()
    return render(request, 'repositorio/alumno_form.html', {'form': form})

@login_required
def alumnoActualizar (request,id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumno')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'repositorio/alumno_form.html', {'form': form})

@login_required
def alumnoEliminar (request,id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    alumno.delete()
    return redirect('alumno')

#______________ Curso

@login_required
def curso(request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render(request, "repositorio/curso.html", contexto)

#Formularios Curso

@login_required
def curso_create(request):
   if request.method == 'POST':
       form = CursoForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('curso')
   else:
       form = CursoForm()
   return render(request, 'repositorio/curso_form.html', {'form': form})
    
@login_required    
def cursosActualizar (request,id_curso):
    curso = Curso.objects.get(id=id_curso)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso')
    else:
        form = CursoForm(instance=curso)        
    return render(request, 'repositorio/curso_form.html', {'form': form})

@login_required
def cursosEliminar (request,id_curso):
    curso = Curso.objects.get(id=id_curso)
    curso.delete()
    contexto = {"cursos": Curso.objects.all()}
    return redirect('curso')

#______________ Acerca de mi

@login_required
def acerca(request):
    return render(request, "repositorio/acerca.html")


#______________ Formulario contacto

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # vuelve a la página de inicio el usuario
    else:
        form = ContactoForm()
    return render(request, 'repositorio/contacto.html', {'form': form})

#______________ Login, Logout, Registro

def loginRequest (request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave) #Esto valida si es el usuario y clave
        if user is not None:
            login (request, user) #Aqui realiza el logeo

            # Busca Avatar
            try: 
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = '/media/avatares/default.png'
            finally:
                request.session['avatar'] = avatar

            return render (request, 'repositorio/index.html')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos. Inténtelo de nuevo.')
            return redirect (reverse_lazy ('login') )
    else:
        form = AuthenticationForm()
    return render (request, "repositorio/login.html", {'form': form})

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (reverse_lazy ('home') )
    else:
        form = RegistroForm()
    return render (request, "repositorio/registro.html", {'form': form})

#______________ Editar perfil

@login_required
def editarPerfil (request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm (request.POST)
        if form.is_valid():
            user = User.objects.get(username =usuario)
            user.email = form.cleaned_data.get("email")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return redirect (reverse_lazy('home'))
    else:
        form = UserEditForm(instance=usuario)
    return render (request, "repositorio/editarPerfil.html", {'form': form})

class EditarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = 'repositorio/editar_clave.html'
    success_url =reverse_lazy('home')

@login_required
def addAvatar (request):
    usuario = request.user
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username =request.user)
            imagen = form.cleaned_data['imagen']
            #____ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len (avatarViejo) > 0 :
                for i in range (len(avatarViejo)):
                    avatarViejo [i].delete ()
            
            #____ Guardar avatares
            avatar = Avatar (user=usuario, imagen=imagen)
            avatar.save()

            #____ Enviar imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session ['avatar']=imagen
            return redirect (reverse_lazy('home'))
    else:
        form = AvatarForm()
    return render (request, "repositorio/addAvatar.html", {'form': form})

# ____________________________________ Código que fue reemplazado ____________________________________ 
# Era porque intente hacer el código del CBV (Class Based Views)
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