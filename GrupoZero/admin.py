from django.contrib import admin
from .models import PerfilUsuario, Rol, Categoria, EstadoObra, Obra, ImagenObra

# Register your models here.

admin.site.register(PerfilUsuario)
admin.site.register(Rol)
admin.site.register(Categoria)
admin.site.register(EstadoObra)
admin.site.register(Obra)
admin.site.register(ImagenObra)