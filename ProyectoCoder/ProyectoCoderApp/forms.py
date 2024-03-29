from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Avatar




class posteoCrear(forms.Form):
    titulo = forms.CharField(max_length=20)
    cuerpo = forms.CharField(max_length=200)   
    fecha = forms.DateField()
    imagen = forms.ImageField(label="Imagen", required=False)
    
    

roles = [("usuario", "usuario"), ("administrador", "administrador")]
class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

      

