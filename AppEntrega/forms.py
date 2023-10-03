from django import forms
 
class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
class buscarCurso(forms.Form):
    curso = forms.CharField()