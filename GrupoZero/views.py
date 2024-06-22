import time

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import PerfilUsuario, Rol

# Create your views here.

def principal(request):
    context={}
    return render(request, 'GrupoZero/principal.html',context)

def perfil_usuario(request):
    context={}
    return render(request, 'GrupoZero/perfil_usuario.html',context)

def perfil_admin(request):
    context={}
    return render(request, 'GrupoZero/perfil_admin.html',context)

def detalle_obra(request):
    context={}
    return render(request, 'GrupoZero/detalle_obra.html',context)

def detalle_autor(request):
    context={}
    return render(request, 'GrupoZero/detalle_autor.html',context)

def detalle_autor2(request):
    context={}
    return render(request, 'GrupoZero/detalle_autor2.html',context)

def detalle_autor3(request):
    context={}
    return render(request, 'GrupoZero/detalle_autor3.html',context)

def blog(request):
    context={}
    return render(request, 'GrupoZero/blog.html',context)

def base(request):
    context={}
    return render(request, 'GrupoZero/base.html',context)

def registro_inicio_sesion(request):
    if request.method == 'POST':
        print(request.POST)
        accion = request.POST.get('accion', None)
        # Verifica si se está realizando un registro o un inicio de sesión
        
        if accion == 'registro':
            print("'Registro' está en request.POST ")
            # Registro de nuevo usuario
            email = request.POST.get('email_registro')
            nombre_completo = request.POST.get('nombre_registro')
            password = request.POST.get('contrasena_registro')

            # Dividir el nombre completo en nombre y apellido
            nombre_apellido = nombre_completo.rsplit(maxsplit=1)  # Divide solo en la última aparición del espacio

            if len(nombre_apellido) == 2:
                first_name, last_name = nombre_apellido
            else:
                first_name = nombre_completo
                last_name = ''

            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name) 

            #Crear perfil para el usuario recién creado, donde se añadirán más campos
            rol=Rol.objects.get(cod_rol=2)
            perfil_usuario = PerfilUsuario( user=user, rol=rol) 
            perfil_usuario.save()

            logout(request)
            user = authenticate(request, username=email, password=password) 

            if user is not None:
                login(request, user)                
                #Obtener el objeto de tipo PerfilUsuario asociado al user recién autenticado
                perfil_usuario = PerfilUsuario.objects.get(user=user)
                #Obtener el rol de ese objeto de tipo PerfilUsuario
                rol = perfil_usuario.rol.cod_rol
                # Redirige al usuario a la página correspondiente a su perfil después del inicio de sesión
                if rol==1:
                    return redirect('perfil_admin')
                elif rol ==2:
                    return redirect('perfil_usuario')
            
        elif accion == 'inicio_sesion':
            print("'Inicio_sesion' está en request.POST ")
            # Inicio de sesión de usuario existente
            email = request.POST.get('email_inicio_sesion')
            password = request.POST.get('contrasena_inicio_sesion')
            logout(request)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)                
                #Obtener el objeto de tipo PerfilUsuario asociado al user recién autenticado
                perfil_usuario = PerfilUsuario.objects.get(user=user)
                #Obtener el rol de ese objeto de tipo PerfilUsuario
                rol = perfil_usuario.rol.cod_rol
                # Redirige al usuario a la página correspondiente a su perfil después del inicio de sesión
                if rol==1:
                    return redirect('perfil_admin')
                elif rol ==2:
                    return redirect('perfil_usuario')
            else:
                # El inicio de sesión falló, renderiza nuevamente el formulario con un mensaje de error
                
                return render(request, 'GrupoZero/inicio', {'error': 'Inicio de sesión fallido'})
        else:
            print("No se registró ninguna acción. Ni 'registro', ni 'inicio_sesion'")
            return render(request, 'GrupoZero/inicio', {'error': 'Inicio de sesión fallido'})
    else:
        # Si el método no es POST, simplemente renderiza el formulario
        return render(request, 'GrupoZero/inicio')
