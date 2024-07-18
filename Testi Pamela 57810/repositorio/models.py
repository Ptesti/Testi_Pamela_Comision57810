from django.db import models

# Modelo de negocio de la aplicación.

# Modelo de Alumno
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

# Modelo de Profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

# Modelo de Materia
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ["nombre", "codigo"]

    def __str__(self):
        return f"{self.nombre}, {self.nombre.codigo}"

# Modelo de Curso
class Curso(models.Model):
    TURNOS = [
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('vespertino', 'Vespertino'),
    ]

    nombre = models.CharField(max_length=100)
    division = models.CharField(max_length=10)
    turno = models.CharField(max_length=50, choices=TURNOS)

    class Meta:
        ordering = ["nombre", "division", "turno"]
    
    def __str__(self):
        return f"{self.nombre} - {self.division} ({self.get_turno_display()})"

# Modelo Contacto
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    