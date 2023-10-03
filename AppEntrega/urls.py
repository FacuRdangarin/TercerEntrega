from django.urls import path
from AppEntrega import views

urlpatterns = [
    path('inicio/',views.inicio,name='Padre'),
    path('curso/',views.curso,name='Cursos'),
    path('profesores/',views.profesores,name='Profesores'),
    path('alumnos/',views.estudiantes,name='Estudiantes'),
    path('entregables/',views.entregables,name='Entregables'),
    path('nosotros/',views.nosotros,name='Nosotros'),
    path('cursoForm/',views.cursoFormulario,name='cursoForm'),
    path('buscar/',views.buscar,name='Buscar')
]
