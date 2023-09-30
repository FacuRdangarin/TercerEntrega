from datetime import datetime as dt
from django.http import HttpResponse
from django.template import Template, Context,loader

def probando_template(request):

    # Abrimos el archivo html
    mi_html = open('C:/Users/urdan/OneDrive/Escritorio/tercer_entrega/tercer_entrega/tercer_entrega/plantillas/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    plantilla = loader.get_template("index.html")
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

#crear fundiones
def saludo(request):
    return HttpResponse("Hola Django, Coder <br>Hola alumnos")

def diaDeHoy(request,nombre):
    dia = dt.now()
    return HttpResponse(f"Hola {nombre},hoy es: {dia}")
