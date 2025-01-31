# Generated by Django 5.0.6 on 2024-07-17 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0002_alumno_alumnocurso_alumnomateria_alumnoprofesor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='alumnos',
        ),
        migrations.RemoveField(
            model_name='alumnomateria',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='alumnomateria',
            name='materia',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='materias',
        ),
        migrations.RemoveField(
            model_name='alumnoprofesor',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='alumnoprofesor',
            name='materia',
        ),
        migrations.RemoveField(
            model_name='alumnoprofesor',
            name='profesor',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='profesores',
        ),
        migrations.RemoveField(
            model_name='cursomateria',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='cursomateria',
            name='materia',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='materias',
        ),
        migrations.RemoveField(
            model_name='cursoprofesor',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='cursoprofesor',
            name='materia',
        ),
        migrations.RemoveField(
            model_name='cursoprofesor',
            name='profesor',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='profesores',
        ),
        migrations.RemoveField(
            model_name='materiaprofesor',
            name='materia',
        ),
        migrations.RemoveField(
            model_name='materiaprofesor',
            name='profesor',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='materias',
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ['apellido', 'nombre'], 'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='mail',
            new_name='email',
        ),
        migrations.DeleteModel(
            name='AlumnoCurso',
        ),
        migrations.DeleteModel(
            name='AlumnoMateria',
        ),
        migrations.DeleteModel(
            name='AlumnoProfesor',
        ),
        migrations.DeleteModel(
            name='CursoMateria',
        ),
        migrations.DeleteModel(
            name='CursoProfesor',
        ),
        migrations.DeleteModel(
            name='MateriaProfesor',
        ),
    ]
