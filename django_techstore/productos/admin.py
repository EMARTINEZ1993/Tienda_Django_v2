from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Producto, Categoria, Carrito, Orden

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(Orden)