from django.urls import path

from AppCoder.models import Curso
from django.contrib.auth.views import LogoutView

from .views import CursoCreate,CursoDelete,CursoDetail, CursoList, CursoUpdate, buscar, busqueda_camada, crea_profesor,listaEntregables,crea_entregable, curso, cursoFormulario, editar_profesores, eliminarProfesores, inicio, listaProfesores, lista_curso, cursos, loginview, profesores, estudiantes, entregables, register, editarPerfil

urlpatterns = [
    path("Agrega-curso/<nombre>/<camada>", curso),
    path("", inicio,name="Inicio"),
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
    path("lista_entregable/", listaEntregables,name="listaEntregables"),
    path("crea-entregable/", crea_entregable,name="CreaEntregable"),
    path("elimina-profesor/<int:id>", eliminarProfesores,name="EliminaProfesor"),
    path("editar-profesor/<int:id>", editar_profesores,name="EditarProfesor"),
    path("listaCursos", CursoList.as_view(),name="ListaCursos"),
    path("detalleCurso/<pk>",CursoDetail.as_view(),name="DetalleCurso"),
    path("creaCurso/",CursoCreate.as_view(),name="CreaCurso"),
    path("actualizarCursos/<pk>",CursoUpdate.as_view(),name="ActualizaCurso"),
    path("eliminarCursos/<pk>",CursoDelete.as_view(),name="EliminaCurso"),
    path("login/",loginview,name="Login"),
    path("registrar/",register,name="Registrar"),
    path("logout/",LogoutView.as_view(template_name="logout.html"),name="Logout"),
    path("editar-perfil/",editarPerfil,name="EditarPerfil"),
]