from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', campo, name="campo"),
    path('login', login_request, name="login"), # no usar login como nombre de la vista
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    

    
   
    path('posteos', posteos, name="posteos"),
    path('crearPosteos/' , crearPosteos , name = "crearPosteos"),

   


    # path('base/', base),
]