#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('perfil_usuario.html', views.perfil_usuario, name='perfil_usuario'),
    path('perfil_admin.html', views.perfil_admin, name='perfil_admin'),
    path('detalle_obra.html', views.detalle_obra, name='detalle_obra'),
    path('detalle_autor.html', views.detalle_autor, name='detalle_autor'),
    path('detalle_autor2.html', views.detalle_autor2, name='detalle_autor2'),
    path('detalle_autor3.html', views.detalle_autor3, name='detalle_autor3'),
    path('blog.html', views.blog, name='blog'),
    path('base.html', views.base, name='base'),
    path('registro-inicio-sesion/', views.registro_inicio_sesion, name='registro_inicio_sesion'),
]