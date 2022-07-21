from django.contrib import admin

from .models import *



class posteoAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'cuerpo','fecha' , 'imagen')





admin.site.register(Posteo, posteoAdmin)

