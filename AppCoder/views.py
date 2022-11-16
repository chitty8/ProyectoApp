from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Equipo, Jugadores, Avatar
from .forms import EquipoFormulario, JugadorFormulario, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin



def aboutme(request):

    return render(request, "aboutme.html",)




def equipo(request,nombre,ciudad):

    equipo = Equipo(nombre=nombre, ciudad=ciudad)
    equipo.save()

    return HttpResponse(f"""
        <p>Curso: {equipo.nombre} - ciudad: {equipo.ciudad} agregado! </p>
    """)


def lista_equipos(request):

    lista = Equipo.objects.all()

    return render(request, "Lista_equipos.html", {"lista_equipos":lista})




def inicio(request):

    avatar = Avatar.objects.get(user=request.user)
    return render(request, "inicio.html", {"url": avatar.imagen.url})


def equipos(request):
    lista = Equipo.objects.all()
    return render(request, "equipos.html", {"lista_equipos":lista})


def jugadores(request):
    lista = Jugadores.objects.all()
    return render(request, "jugadores.html", {"jugadores":lista})


def equipoFormulario(request):

    print("method", request.method)
    print("post", request.POST)

    if request.method == "POST":
        mi_formulario = EquipoFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            equipo= Equipo(nombre=data["equipo"], ciudad=data["ciudad"], equipo=data["equipo"], nacimiento=data["nacimiento"])
            equipo.save()

        return redirect("Equipos")
    
    else:
        mi_formulario = EquipoFormulario()


        return render(request, "equipoFormulario.html", {"mi_formulario":mi_formulario})
    

def busqueda_ciudad(request):

    return render(request, "busqueda_ciudad.html")

def buscar(request):

    ciudad_buscada = request.GET["ciudad"]
    
    equipo = Equipo.objects.get(ciudad = ciudad_buscada)

    return render(request, "resultado_busqueda.html", {"equipo":equipo, "ciudad": ciudad_buscada})


    
def listaJugadores(request):
    
    jugadores = Jugadores.objects.all()

    return render(request, "leerjugadores.html", {"jugadores": jugadores})




def crea_jugadores(request):

    print("method", request.method)
    print("post", request.POST)

    if request.method == "POST":
        miformulario = JugadorFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid():

            data = miformulario.cleaned_data
             
            jugador= Jugadores(nombre=data["nombre"], apellido=data["apellido"], gmail=data["gmail"],equipo=data["equipo"], nacimiento=data["nacimiento"] )
            jugador.save()

        return HttpResponseRedirect("/app-coder/")
    
    else:
        miformulario = JugadorFormulario()


        return render(request, "jugadorFormulario.html", {"miformulario":miformulario})
    

def eliminarJugadores(request,id):
    if request.method == "POST":

        jugadores = Jugadores.objects.get(id=id)
        jugadores.delete()

        jugadores = Jugadores.objects.all()

        
    return render(request, "leerJugadores.html", {"jugadores":jugadores})


def editar_jugadores(request, id):

    print("method", request.method)
    print("post", request.POST)

    jugador = Jugadores.objects.get(id=id)

    if request.method == "POST":

        miFormulario = JugadorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            jugador.nombre = data["nombre"]
            jugador.apellido = data["apellido"]
            jugador.gmail = data["gmail"]
            

            jugador.save()

        return HttpResponseRedirect("/app-coder/")
    
    else:
        miFormulario = JugadorFormulario( initial={
            "nombre":jugador.nombre,
            "apellido":jugador.apellido,
            "gmail":jugador.gmail,
            
        })


        return render(request, "editarJugador.html", {"miFormulario":miFormulario, "id": jugador.id})
    



class EquipoList(LoginRequiredMixin,ListView):

    model = Equipo
    template_name = "equipo_list.html" 
    context_object_name = "equipos"

class EquipoDetail(DetailView):
    model = Equipo
    template_name = "equipo_detail.html" 
    context_object_name = "equipo"

class EquipoCreate(CreateView):
    model = Equipo
    template_name = "equipo_create.html" 
    fields = ["nombre", "ciudad"]
    success_url =  "/app-coder/"
 
class EquipoUpdate(UpdateView):
    model = Equipo
    template_name = "equipo_update.html" 
    fields = ("__all__")
    success_url =  "/app-coder/"

class EquipoDelete(DeleteView):         
    model = Equipo
    template_name = "equipo_delete.html" 
    success_url =  "/app-coder/"



def loginview(request):
    print("method", request.method)
    print("post", request.POST)

    
    if request.method == "POST":
        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request,user,psw)
                
                return render(request,"inicio.html", {"mensaje":f"bienvenido {usuario}"} )
            
            else:

                return render(request,"inicio.html", {"mensaje":f"Erro datos incorrectos "} )
             
        return render(request,"inicio.html", {"mensaje":f"Error, formulario invalido"} )
    
    else:
        miFormulario = AuthenticationForm()


        return render(request, "login.html", {"miFormulario":miFormulario})



def register(request):

    print("method", request.method)
    print("post", request.POST)

    
    if request.method == "POST":
        miFormulario = UserCreationForm(request.POST)

        if miFormulario.is_valid():

            username = miFormulario.cleaned_data["username"]

            miFormulario.save()

            return render(request,"inicio.html", {"mensaje":f"Usuario {username} creado con exito"} )

        else:
            return render(request,"inicio.html", {"mensaje":f"Error al crear usuario"} ) 
        
    else:
         miFormulario = UserCreationForm()

         return render(request, "registro.html", {"miFormulario":miFormulario})
    


def editarPerfil(request):
    
    print('method:', request.method)
    print('post: ', request.POST)

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            

            usuario.save()

            return render(request, "inicio.html", {"mensaje": f'Datos actualizados!'})

        return render(request,"editarPerfil.html", {"mensaje":f"Las contraseñas no coinciden"})
    else:

        miFormulario = UserEditForm(instance=request.user)

        return render(request, "editarPerfil.html", {"miFormulario": miFormulario})
    
