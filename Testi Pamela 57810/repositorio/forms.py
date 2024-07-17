from django import forms
from .models import *

class AlumnoForm(forms.ModelForm):
    curso = forms.ChoiceField(choices=Curso.Cursos)
    turno = forms.ChoiceField(choices=Curso.Turnos)

    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'materias', 'profesores', 'curso','turno']

class ProfesorForm(forms.ModelForm):
    curso = forms.ChoiceField(choices=Curso.Cursos)
    turno = forms.ChoiceField(choices=Curso.Turnos)
    
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'materias', 'cursos', 'mail']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'division', 'turno', 'alumnos', 'profesores', 'materias']

class CursoProfesorForm(forms.ModelForm):
    materia = forms.ModelChoiceField(queryset=Materia.objects.all())

    class Meta:
        model = CursoProfesor
        fields = ['curso', 'materia']

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'codigo']