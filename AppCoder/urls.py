from django.urls import path

from .views import buscar, busqueda_camada, curso, cursoFormulario, inicio, lista_curso, cursos, profesores, estudiantes, entregables

urlpatterns = [
    path("Agrega-curso/<nombre>/<camada>", curso),
    path("inicio", inicio),
    path("lista_curso/", lista_curso),
    path("cursos/", cursos, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiantes,name="Estudiantes"),
    path("entregables/", entregables,name="Entregables"),
    path("cursoFormulario/", cursoFormulario,name="CursoFormulario"),
    path("busquedacamada/", busqueda_camada,name="busqueda_camada"),
    path("buscar/", buscar,name="buscar"),
]