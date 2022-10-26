from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso



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

    return HttpResponse("Vista inicio")

def cursos(request):

    return render(request, "cursos.html")

    return HttpResponse("Vista cursos")

def profesores(request):

    return render(request, "profesores.html")

    return HttpResponse("Vista profesores")

def estudiantes(request):

    return render(request, "estudiantes.html")

    return HttpResponse("Vista estudiantes")

def entregables(request):

    return render(request, "entregables.html")

    return HttpResponse("Vista entregables")