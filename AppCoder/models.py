from django.db import models




class Curso(models.Model):

    nombre = models.CharField( max_length=50)
    camada = models.IntegerField()

class Estudiantes(models.Model):

    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    gmail = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    gmail = models.EmailField()
    profesion = models.CharField( max_length=50)


class Entregables(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()