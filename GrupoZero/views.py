import time

from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import PerfilUsuario, Rol

# Create your views here.

def principal(request):
    perfiles_usuarios = PerfilUsuario.objects.filter(rol__cod_rol=2)

    for perfil in perfiles_usuarios:
        print(perfil.user.get_full_name())

    context = {
        'perfiles_usuarios': perfiles_usuarios
    }
    return render(request, 'GrupoZero/principal.html',context)

def perfil_usuario(request):
    perfiles_usuarios = PerfilUsuario.objects.filter(rol__cod_rol=2)

    for perfil in perfiles_usuarios:
        print(perfil.user.get_full_name())

    context = {
        'perfiles_usuarios': perfiles_usuarios
    }
    return render(request, 'GrupoZero/perfil_usuario.html',context)

def perfil_admin(request):
    perfiles_usuarios = PerfilUsuario.objects.filter(rol__cod_rol=2)

    for perfil in perfiles_usuarios:
        print(perfil.user.get_full_name())

    context = {
        'perfiles_usuarios': perfiles_usuarios
    }
    return render(request, 'GrupoZero/perfil_admin.html',context)

def detalle_obra(request):
    perfiles_usuarios = PerfilUsuario.objects.filter(rol__cod_rol=2)

    for perfil in perfiles_usuarios:
        print(perfil.user.get_full_name())

    context = {
        'perfiles_usuarios': perfiles_usuarios
    }
    return render(request, 'GrupoZero/detalle_obra.html',context)

def detalle_autor(request, username):
    user = get_object_or_404(User, username=username)
    perfil_usuario = get_object_or_404(PerfilUsuario, user=user)

    # Obtener todos los perfiles de usuarios con rol cod_rol=2 para el desplegable del navbar
    perfiles_usuarios = PerfilUsuario.objects.filter(rol__cod_rol=2)

    context = {
        'perfil_usuario': perfil_usuario,
        'perfiles_usuarios': perfiles_usuarios,  # Agregar la lista de perfiles para el navbar
    }
    return render(request, 'GrupoZero/detalle_autor.html',context)

def detalle_autor2(request):
    context={}
    return render(request, 'GrupoZero/detalle_autor2.html',context)

def detalle_autor3(request):
    context={}
    return render(request, 'GrupoZero/detalle_autor3.html',context)

def blog(request):
    perfiles_usuarios = PerfilUsuario.objects.filter(rol__cod_rol=2)

    for perfil in perfiles_usuarios:
        print(perfil.user.get_full_name())

    context = {
        'perfiles_usuarios': perfiles_usuarios
    }
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
                
                return render(request, 'GrupoZero/principal.html', {'error': 'Inicio de sesión fallido'})
        else:
            print("No se registró ninguna acción. Ni 'registro', ni 'inicio_sesion'")
            return render(request, 'GrupoZero/principal.html', {'error': 'Inicio de sesión fallido'})
    else:
        # Si el método no es POST, simplemente renderiza el formulario
        return render(request, 'GrupoZero/principal.html')
    

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')
        descripcion = request.POST.get('descr')
        imagen = request.FILES.get('imagen')

        user = request.user

        if nombre:
            nombre_split = nombre.split()
            if len(nombre_split) > 1:
                user.first_name = nombre_split[0]
                user.last_name = ' '.join(nombre_split[1:])
            else:
                user.first_name = nombre_split[0]
                user.last_name = ''
            
        if email:
            user.email = email
            user.username = email
        
        if password:
            user.set_password(password)
        
        user.save()

        perfilUsuario, created = PerfilUsuario.objects.get_or_create(user=user)
        if descripcion:
            perfilUsuario.descripcion = descripcion
        if imagen:
            perfilUsuario.imagen = imagen
        
        perfilUsuario.save()

        return redirect('perfil_usuario')  # Redirigir a una página de perfil después de la actualización
    

    return render(request, 'GrupoZero/perfil_usuario.html')


@login_required
def get_desc(request):
    user = request.user
    try:
        miau = PerfilUsuario.objects.get(user=user)
        descripcion = miau.descripcion if miau.descripcion else "No hay descripción disponible."
    except PerfilUsuario.DoesNotExist:
        descripcion = "No hay descripción disponible."

    context = {
        'user': user,
        'descripcion_perfil': descripcion,
    }

    return render(request, 'GrupoZero/perfil_usuario.html', context) 


@login_required
def perfil_usuario(request):
    perfil_usuario = get_object_or_404(PerfilUsuario, user=request.user)
    return render(request, 'GrupoZero/perfil_usuario.html', {'perfil_usuario': perfil_usuario})


def get_usuario_artista():
    # Obtener todos los perfiles de usuarios con rol cod_rol=2
    perfiles_usuarios = PerfilUsuario.objects.filter(rol__cod_rol=2)

    for perfil in perfiles_usuarios:
        print(perfil.user.get_full_name())

    context = {
        'perfiles_usuarios': perfiles_usuarios
    }

    return context

