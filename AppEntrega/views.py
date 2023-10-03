from django.shortcuts import render
from AppEntrega.forms import CursoFormulario,buscarCurso
from AppEntrega.models import Curso
#from django.http import HttpResponse 


def inicio(request):
    return render(request, "AppEntrega/padre.html")

def curso(request):
    return render(request,"AppEntrega/curso.html")

def profesores(request):
    return render(request,"AppEntrega/profesores.html")

def estudiantes(request):
    return render(request,"AppEntrega/estudiantes.html")

def entregables(request):
    return render(request,"AppEntrega/entregables.html")

def nosotros(request):
    return render(request,"AppEntrega/nosotros.html")

 
def cursoFormulario(request):
 
    if request.method == "POST":
 
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos = Curso(curso=informacion['curso'], camada=informacion['camada'])
            cursos.save()
            return render(request, "AppEntrega/index.html")
    else:
        miFormulario = CursoFormulario()
 
    return render(request, "AppEntrega/cursoFormulario.html", {"miFormulario": miFormulario})


def buscar(request):
    if request.method == "POST":
 
        miFormulario = buscarCurso(request.POST) 
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos = Curso.objects.filter(curso__icontains=informacion['curso'])
            return render(request, "AppEntrega/lista.html",{'cursos':cursos})
        else:
            pass
    else:
        miFormulario = buscarCurso()
 
    return render(request, "AppEntrega/cursoFormulario.html", {"miFormulario": miFormulario})

