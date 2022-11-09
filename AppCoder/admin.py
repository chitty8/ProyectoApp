from django.contrib import admin

from .models import Curso, Profesor, Avatar, Entregables,Estudiantes

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Avatar)
admin.site.register(Entregables)
admin.site.register(Estudiantes)