from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Curso, Profesor, Avatar
from .forms import CursoFormulario, ProfesorFormulario, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin




def curso(request,nombre,camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado! </p>
    """)


def lista_curso(request):

    lista = Curso.objects.all()

    return render(request, "Lista_cursos.html", {"lista_cursos":lista})




def inicio(request):

    avatar = Avatar.objects.get(user=request.user)
    return render(request, "inicio.html", {"url": avatar.imagen.url})

@login_required
def cursos(request):
    lista = Curso.objects.all()
    return render(request, "cursos.html", {"lista_cursos":lista})

@staff_member_required(login_url="/app-coder/login")
def profesores(request):
    lista = Profesor.objects.all()
    return render(request, "profesores.html", {"profesores":lista})


def estudiantes(request):

    return render(request, "estudiantes.html")


def entregables(request):

    return render(request, "entregables.html")



def cursoFormulario(request):

    print("method", request.method)
    print("post", request.POST)

    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            curso= Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()

        return redirect("Cursos")
    
    else:
        mi_formulario = CursoFormulario()


        return render(request, "cursoFormulario.html", {"mi_formulario":mi_formulario})
    

def busqueda_camada(request):

    return render(request, "busqueda_camada.html")

def buscar(request):

    camada_buscada = request.GET["camada"]
    
    curso = Curso.objects.get(camada = camada_buscada)

    return render(request, "resultado_busqueda.html", {"curso":curso, "camada": camada_buscada})


    
def listaProfesores(request):
    
    profesores = Profesor.objects.all()

    return render(request, "leerProfesores.html", {"profesores": profesores})


def crea_profesor(request):

    print("method", request.method)
    print("post", request.POST)

    if request.method == "POST":
        miformulario = ProfesorFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid():

            data = miformulario.cleaned_data
             
            profesor= Profesor(nombre=data["nombre"], apellido=data["apellido"], gmail=data["gmail"], profesion=data["profesion"])
            profesor.save()

        return HttpResponseRedirect("/app-coder/")
    
    else:
        miformulario = ProfesorFormulario()


        return render(request, "profesorFormulario.html", {"miformulario":miformulario})
    


def eliminarProfesores(request,id):
    if request.method == "POST":

        profesor = Profesor.objects.get(id=id)
        profesor.delete()

        profesores = Profesor.objects.all()

        
    return render(request, "leerProfesores.html", {"profesores":profesores})


def editar_profesores(request, id):

    print("method", request.method)
    print("post", request.POST)

    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.gmail = data["gmail"]
            profesor.profesion = data["profesion"]

            profesor.save()

        return HttpResponseRedirect("/app-coder/")
    
    else:
        miFormulario = ProfesorFormulario( initial={
            "nombre":profesor.nombre,
            "apellido":profesor.apellido,
            "gmail":profesor.gmail,
            "profesion":profesor.profesion,
        })


        return render(request, "editarProfesor.html", {"miFormulario":miFormulario, "id": profesor.id})
    



class CursoList(LoginRequiredMixin,ListView):

    model = Curso
    template_name = "curso_list.html" 
    context_object_name = "cursos"

class CursoDetail(DetailView):
    model = Curso
    template_name = "curso_detail.html" 
    context_object_name = "curso"

class CursoCreate(CreateView):
    model = Curso
    template_name = "curso_create.html" 
    fields = ["nombre", "camada"]
    success_url =  "/app-coder/"
 
class CursoUpdate(UpdateView):
    model = Curso
    template_name = "curso_update.html" 
    fields = ("__all__")
    success_url =  "/app-coder/"

class CursoDelete(DeleteView):         
    model = Curso
    template_name = "curso_delete.html" 
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
    
