from django.urls import path

from .views import curso, inicio, lista_curso, cursos, profesores, estudiantes, entregables

urlpatterns = [
    path("Agrega-curso/<nombre>/<camada>", curso),
    path("", inicio),
    path("lista_curso/", lista_curso),
    path("cursos/", cursos, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiantes,name="Estudiantes"),
    path("entregables/", entregables,name="Entregables"),
]