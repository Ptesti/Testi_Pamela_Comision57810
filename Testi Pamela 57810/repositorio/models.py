from django.db import models

# Modelo de negocio de la aplicación.

#modelo de alumno
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cursos = models.ManyToManyField('Curso', through='AlumnoCurso')
    materias = models.ManyToManyField('Materia', through='AlumnoMateria')
    profesores = models.ManyToManyField('Profesor', through='AlumnoProfesor')

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.apellido} {self.nombre} {self.cursos}{self.turno}"

#modelo profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    materias = models.ManyToManyField('Materia', through='MateriaProfesor')
    cursos = models.ManyToManyField('Curso', through='CursoProfesor')
    mail = models.EmailField()

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.apellido} {self.nombre} {self.materias} {self.cursos}"

#modelo materia
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    class Meta: 
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

#modelo curso
class Curso(models.Model):
#opciones de cursos
    Cursos = [
        ('1°1°', '1°1°'),
        ('1°2°', '1°2°'),
        ('1°3°', '1°3°'),
        ('1°4°', '1°4°'),
        ('2°1°', '2°1°'),
        ('2°2°', '2°2°'),
        ('2°3°', '2°3°'),
        ('2°4°', '2°4°'),
        ('3°1°', '3°1°'),
        ('3°2°', '3°2°'),
        ('3°3°', '3°3°'),
        ('3°4°', '3°4°'),
        ('4°1°', '4°1°'),
        ('4°2°', '4°2°'),
        ('4°3°', '4°3°'),
        ('4°4°', '4°4°'),
        ('5°1°', '5°1°'),
        ('5°2°', '5°2°'),
        ('5°3°', '5°3°'),
        ('5°4°', '5°4°'),
        ('6°1°', '6°1°'),
        ('6°2°', '6°2°'),
        ('6°3°', '6°3°'),
        ('6°4°', '6°4°'),
    ]

#opciones de turnos   
    Turnos = [
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('vespertino', 'Vespertino'),
    ]

    nombre = models.CharField(max_length=100)
    division = models.CharField(max_length=10, choices=Cursos)
    turno = models.CharField(max_length=50, choices=Turnos)
    alumnos = models.ManyToManyField(Alumno, through='AlumnoCurso')
    profesores = models.ManyToManyField(Profesor, through='CursoProfesor')
    materias = models.ManyToManyField(Materia, through='CursoMateria')

    def __str__(self):
        return f"{self.nombre} - {self.division} ({self.get_turno_display()})"

#modelo relación alumno materia
class AlumnoMateria(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

#modelo relación alumno profesor
class AlumnoProfesor(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

#modelo relación alumno curso
class AlumnoCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

#modelo relación curso profesor
class CursoProfesor(models.Model):
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

#modelo relación curso materia
class CursoMateria(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

#modelo relacion materia profesor
class MateriaProfesor(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)