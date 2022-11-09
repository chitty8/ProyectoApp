from django import forms
from django import forms
from django.contrib.auth.forms import  UserChangeForm,UserCreationForm
from django.contrib.auth.models import User
 
   # TODO: Define form fields here


class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()
     

class ProfesorFormulario(forms.Form):

     nombre = forms.CharField(max_length=30)
     apellido = forms.CharField(max_length=30)
     gmail = forms.EmailField()
     profesion = forms.CharField(max_length=30)


class EntregableFormulario(forms.Form):

     nombre = forms.CharField(max_length=30)
     fechaDeEntrega = forms.CharField(max_length=30)
     entregado = forms.BooleanField()
     link = forms.CharField(max_length=250)
    


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


    def clean_password2(self):

        print('self\n',self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2
    

class UserRegisterForm(UserCreationForm):

    class Meta:

        model = User
        fields = ('username', 'last_name', 'first_name', 'email')