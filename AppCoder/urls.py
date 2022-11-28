from django.urls import path

from AppCoder.models import Equipo
from django.contrib.auth.views import LogoutView

from .views import EquipoCreate,EquipoDelete,EquipoDetail, EquipoList, EquipoUpdate, aboutme, buscar, busqueda_ciudad, crea_jugadores, equipo, equipoFormulario, editar_jugadores, eliminarJugadores, inicio, listaJugadores, lista_equipos, equipos, loginView, jugadores, register, editarPerfil

urlpatterns = [
    path("Agrega-equipo/<nombre>/<ciudad>", equipo),
    path("", inicio,name="Inicio"),
    path("lista_equipo/", lista_equipos),
    path("equipos/", equipos, name="Equipos"),
    path("jugadores/", jugadores, name="Jugadores",),
    path("equipoFormulario/", equipoFormulario,name="EquipoFormulario"),
    path("busquedaciudad/", busqueda_ciudad,name="busqueda_ciudad"),
    path("buscar/", buscar,name="buscar"),
    path("listaJugadores/", listaJugadores,name="listaJugadores"),
    path("crea-Jugadores/", crea_jugadores,name="CreaJugador"),
    path("elimina-jugador/<int:id>", eliminarJugadores,name="EliminaJugador"),
    path("editar-jugador/<int:id>", editar_jugadores,name="EditarJugador"),
    path("listaEquipos", EquipoList.as_view(),name="ListaEquipos"),
    path("detalleEquipo/<pk>",EquipoDetail.as_view(),name="DetalleEquipo"),
    path("creaEquipo/",EquipoCreate.as_view(),name="CreaEquipo"),
    path("actualizarEquipo/<pk>",EquipoUpdate.as_view(),name="ActualizaEquipo"),
    path("eliminarEquipo/<pk>",EquipoDelete.as_view(),name="EliminaEquipo"),
    path("login/",loginView,name="Login"),
    path("registrar/",register,name="Registrar"),
    path("logout/",LogoutView.as_view(template_name="logout.html"),name="Logout"),
    path("editar-perfil/",editarPerfil,name="EditarPerfil"),
    path("AboutMe/",aboutme,name="AboutMe")
]