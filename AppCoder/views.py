from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from django.views.generic.detail import





# Create your views here.

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
    
    return render(request, "inicio.html")


def cursos(request):
    lista = Curso.objects.all()
    return render(request, "cursos.html", {"lista_cursos":lista})


def profesores(request):

    return render(request, "profesores.html")


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
        mi_formulario = ProfesorFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            profesor= Profesor(nombre=data["nombre"], apellido=data["apellido"], gmail=data["email"], profesion=data["profesion"])
            profesor.save()

        return HttpResponseRedirect("/app-coder/")
    
    else:
        miformulario = ProfesorFormulario()


        return render(request, "profesorFormulario", {"miformulario":miformulario})
    


def eliminarProfesores(request):
    if request.method == "POST":
        profesor = Profesor.objects.get(id=id)
        profesor.delete
        profesores = Profesor.objects.all()

        return HttpResponseRedirect("/app-code/")
        
    return render(request, "leerProfesores.html", {"profesores":profesores})


def edutar_profesores(request):

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
            profesor.gmail = data["email"]
            profesor.profesion = data["profesion"]

            profesor.save()

        return HttpResponseRedirect("/app-coder/")
    
    else:
        miformulario = ProfesorFormulario( initial= {
            "nombre":profesor.nombre,
            "apellido":profesor.apellido,
            "email":profesor.email,
            "profesion":profesor.profesion,
        })


        return render(request, "profesorFormulario", {"miformulario":miformulario})
    



class CursoList(ListView):

    model = Curso
    template_name = "curso_list.html" 
    context_object_name = "cursos"

class CursoDetail(ListView):
    model = Curso
    template_name = "curso_detail.html" 
      
class CursoCreate(ListView):
    model = Curso
    template_name = "curso_create.html" 
   
class CursoUpdate(ListView):
    model = Curso
    template_name = "curso_update.html" 
        

class CursoDelete(ListView):         
    model = Curso
    template_name = "curso_delete.html" 