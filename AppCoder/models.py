from django.db import models
from django.contrib.auth.models import User



class Equipo(models.Model):

    nombre = models.CharField( max_length=50)
    ciudad = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

class Jugadores(models.Model):

    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    equipo = models.CharField(max_length=50)
    gmail = models.EmailField()
    nacimiento = models.DateField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.equipo}"


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)