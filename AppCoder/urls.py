from django.urls import path

from ProyectoApp.AppCoder.models import Curso

from .views import buscar, busqueda_camada, crea_profesor, curso, cursoFormulario, edutar_profesores, eliminarProfesores, inicio, listaProfesores, lista_curso, cursos, profesores, estudiantes, entregables

urlpatterns = [
    path("Agrega-curso/<nombre>/<camada>", curso),
    path("", inicio),
    path("lista_curso/", lista_curso),
    path("cursos/", cursos, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiantes,name="Estudiantes"),
    path("entregables/", entregables,name="Entregables"),
    path("cursoFormulario/", cursoFormulario,name="CursoFormulario"),
    path("busquedacamada/", busqueda_camada,name="busqueda_camada"),
    path("buscar/", buscar,name="buscar"),
    path("listaProfesores/", listaProfesores,name="listaProfesores"),
    path("crea-profesores/", crea_profesor,name="CreaProfesor"),
    path("elimina-profesor/<int:id>", eliminarProfesores,name="EliminaProfesor"),
    path("edita-profesor/<int:id>", edutar_profesores,name="EditarProfesor"),
    path("listacurso/", Curso.list,name="EditarProfesor"),
]