from django import forms
from django import forms


    # TODO: Define form fields here


class CursoFormulario(forms.Form):

     curso = forms.CharField()
     camada = forms.IntegerField()
     