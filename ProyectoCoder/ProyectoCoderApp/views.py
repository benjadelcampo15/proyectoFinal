import datetime
from distutils.log import INFO

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def campo(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4, 9, 7, 8, 5, 10]

    return render(request, "ProyectoCoderApp/index.html", {"mi_nombre": nombre, "dia_hora": hoy, "notas": notas})


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("campo")
            else:
                return redirect("login")
        else:
            return redirect("login")

    form = AuthenticationForm()

    return render(request, "ProyectoCoderApp/login.html", {"form": form})


def register_request(request):

    if request.method == "POST":

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            # es la primer contraseña, no la confirmacion
            password = form.cleaned_data.get('password1')

            form.save()  # registramos el usuario
            # iniciamos la sesion
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("campo")
            else:
                return redirect("login")

        return render(request, "ProyectoCoderApp/register.html", {"form": form})

    # form = UserCreationForm()
    form = UserRegisterForm()

    return render(request, "ProyectoCoderApp/register.html", {"form": form})


def logout_request(request):
    logout(request)
    return redirect("campo")

# vista de editar perfil


@login_required




def posteos(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            posteos = Posteo.objects.filter(
                Q(nombre__icontains=search) | Q(apellido__icontains=search)).values()
            posteos = Posteo.objects.all()
            return render(request, "ProyectoCoderApp/posteos.html", {"posteos": posteos} )

    posteos = Posteo.objects.all()

    return render(request, "ProyectoCoderApp/posteos.html", {"posteos": posteos})



def crearPosteos(request):
     if request.method == "POST":
        
        formulario = posteoCrear(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            posteo = Posteo(titulo=info["titulo"],cuerpo=info["cuerpo"] , fecha = info["fecha"] , imagen = info["imagen"])
            
            posteo.save()

            return redirect("posteos")

        return render(request,"ProyectoCoderApp/posteos.html",{"form":formulario})

    # get
     formulario = posteoCrear()
     return render(request,"ProyectoCoderApp/posteos.html",{"form":formulario})














def campo(request):

    return render(request, 'ProyectoCoderApp/inicio1.html')
