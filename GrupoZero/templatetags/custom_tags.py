# mi_aplicacion/templatetags/custom_tags.py

from django import template
from GrupoZero.models import PerfilUsuario

register = template.Library()

@register.simple_tag
def obtener_descripcion_perfil(usuario):
    try:
        perfil_usuario = PerfilUsuario.objects.get(user=usuario)
        return perfil_usuario.descripcion if perfil_usuario.descripcion else "No hay descripción disponible."
    except PerfilUsuario.DoesNotExist:
        return "No hay descripción disponible."
    
@register.simple_tag
def obtener_img_perfil(usuario):
    try:
        perfil_usuario = PerfilUsuario.objects.get(user=usuario)
        return perfil_usuario.imagen if perfil_usuario.imagen else None
    except PerfilUsuario.DoesNotExist:
        return None