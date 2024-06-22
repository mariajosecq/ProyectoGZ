#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.principal, name='inicio'),
    path('perfil_usuario', views.perfil_usuario, name='perfil_usuario'),
    path('perfil_admin', views.perfil_admin, name='perfil_admin'),
    path('detalle_obra', views.detalle_obra, name='detalle_obra'),
    path('detalle_autor', views.detalle_autor, name='detalle_autor'),
    path('detalle_autor2', views.detalle_autor2, name='detalle_autor2'),
    path('detalle_autor3', views.detalle_autor3, name='detalle_autor3'),
    path('blog', views.blog, name='blog'),
    path('base', views.base, name='base'),
    path('registro-inicio-sesion', views.registro_inicio_sesion, name='registro_inicio_sesion'),
]