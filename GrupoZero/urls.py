from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('inicio', views.principal, name='inicio'),
    path('perfil_usuario', views.perfil_usuario, name='perfil_usuario'),
    path('perfil_admin', views.perfil_admin, name='perfil_admin'),
    path('detalle_obra//<int:cod_obra>/', views.detalle_obra, name='detalle_obra'),
    path('detalle_autor/<str:username>/', views.detalle_autor, name='detalle_autor'),
    path('detalle_autor2', views.detalle_autor2, name='detalle_autor2'),
    path('detalle_autor3', views.detalle_autor3, name='detalle_autor3'),
    path('blog', views.blog, name='blog'),
    path('base', views.base, name='base'),
    path('registro-inicio-sesion', views.registro_inicio_sesion, name='registro_inicio_sesion'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('get_desc/', views.get_desc, name='get_desc'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('get_usuarios_artistas/', views.get_usuarios_artistas, name='get_usuarios_artistas'),
    path('nueva_obra/', views.nueva_obra, name='nueva_obra'),
    path('get_categorias/', views.get_categorias, name='get_categorias'),
    path('modal_obras/', views.modal_obras, name='modal_obras'),
    path('guardar_cambios_obra/', views.guardar_cambios_obra, name='guardar_cambios_obra'),
    path('eliminar_obra//int:cod_obra>/', views.eliminar_obra, name='eliminar_obra'),
]
