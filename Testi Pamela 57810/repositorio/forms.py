from django import forms
from .models import *

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email']

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'codigo']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'division', 'turno']