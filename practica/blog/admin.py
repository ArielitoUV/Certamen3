from django.contrib import admin
from .models import Cliente,Producto,Calificacion

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Calificacion)
