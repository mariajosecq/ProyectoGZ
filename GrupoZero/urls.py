from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('get_desc/', views.get_desc, name='get_desc'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
