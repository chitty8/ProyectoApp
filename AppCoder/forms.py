from django import forms
from django import forms


    # TODO: Define form fields here


class CursoFormulario(forms.Form):

     curso = forms.CharField()
     camada = forms.IntegerField()
     

     
class ProfesorFormulario(forms.Form):

     nombre = forms.CharField(max_length=30)
     apellido = forms.CharField(max_length=30)
     email = forms.EmailField()
     profesion = forms.CharField(max_length=30)