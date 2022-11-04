from django.db import models
from django.contrib.auth.models import User



class Curso(models.Model):

    nombre = models.CharField( max_length=50)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.camada}"

class Estudiantes(models.Model):

    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    gmail = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    gmail = models.EmailField()
    profesion = models.CharField( max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"



class Entregables(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)