from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseForbidden

from .models import PerfilUsuario, Rol, Obra, EstadoObra, Categoria


# Create your views here.

def principal(request):
    context = get_usuarios_artistas()
    return render(request, 'GrupoZero/principal.html',context)

@login_required
def perfil_usuario(request):
    # Obtener categorías
    categorias = get_categorias()

    # Obtener perfil de usuario actual
    perfil_usuario = get_object_or_404(PerfilUsuario, user=request.user)

    # Obtener perfiles de usuarios artistas
    perfiles_artistas = get_usuarios_artistas()

    # Obtener obras del usuario actual
    obras_usuario = Obra.objects.filter(user=request.user)

    context = {
        'categorias': categorias,
        'perfil_usuario': perfil_usuario,
        'perfiles_artistas': perfiles_artistas,
        'obras_usuario': obras_usuario,
        # Otros datos que necesites pasar al contexto
    }

    return render(request, 'GrupoZero/perfil_usuario.html', context)

@login_required
def perfil_admin(request):
    # Obtener perfil de usuario actual
    perfil_usuario = get_object_or_404(PerfilUsuario, user=request.user)
    
        # Obtener todos los perfiles de usuarios con sus roles
    perfiles_usuarios = PerfilUsuario.objects.all()
    
    # Obtener roles disponibles para el desplegable
    roles = Rol.objects.all()

    if request.method == 'POST':
        for perfil_usuario in perfiles_usuarios:
            rol_nuevo_id = request.POST.get(f'rol_{perfil_usuario.user.username}')
            rol_nuevo = Rol.objects.get(pk=rol_nuevo_id)
            perfil_usuario.rol = rol_nuevo
            perfil_usuario.save()

        return redirect('perfil_admin')
    
    
    obras = Obra.objects.all()  

    if request.method == 'POST':
        for obra in obras:
            estado_nuevo = request.POST.get(f'estado_{obra.cod_obra}')
            obra.estado = EstadoObra.objects.get(pk=estado_nuevo)
            obra.save()

        return redirect('perfil_admin')  # Redirige a la misma página después de guardar cambios

    context = {
        'perfil_usuario': perfil_usuario,
        'perfiles_usuarios': perfiles_usuarios,
        'roles': roles,
        'obras': obras,
        'estados': EstadoObra.objects.all(), 
    }

    return render(request, 'GrupoZero/perfil_admin.html', context)

def detalle_obra(request, cod_obra):
    perfiles_usuarios = PerfilUsuario.objects.filter(rol__cod_rol=2)

    obra = get_object_or_404(Obra, cod_obra=cod_obra)

    for perfil in perfiles_usuarios:
        print(perfil.user.get_full_name())

    context = {
        'perfiles_usuarios': perfiles_usuarios,
        'obra': obra,
    }
    return render(request, 'GrupoZero/detalle_obra.html',context)

def detalle_autor(request, username):
    user = get_object_or_404(User, username=username)
    perfil_usuario = get_object_or_404(PerfilUsuario, user=user)

    # Obtener todos los perfiles de usuarios con rol cod_rol=2 para el desplegable del navbar
    perfiles_usuarios = PerfilUsuario.objects.filter(rol__cod_rol=2)

    obras_autor = Obra.objects.filter(user=perfil_usuario.user, estado__nombre_estado_obra='aprobado')

    obras_aprobadas = perfil_usuario.user.obra_set.filter(estado__nombre_estado_obra='aprobado')
    nro_obras_aprobadas = obras_aprobadas.count()

    context = {
        'perfil_usuario': perfil_usuario,
        'perfiles_usuarios': perfiles_usuarios, 
        'obras_autor': obras_autor,
        'nro_obras_aprobadas': nro_obras_aprobadas,
    }  

    return render(request, 'GrupoZero/detalle_autor.html',context)

def detalle_autor2(request):
    context={}
    return render(request, 'GrupoZero/detalle_autor2.html',context)

def detalle_autor3(request):
    context={}
    return render(request, 'GrupoZero/detalle_autor3.html',context)

def blog(request):
    context = get_usuarios_artistas()
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

        # Redirigir según el rol del perfilUsuario
        if perfilUsuario.rol and perfilUsuario.rol.cod_rol == 1:
            return redirect('perfil_admin') 
        else:
            return redirect('perfil_usuario') 
    else:
        return render(request, 'GrupoZero/inicio.html')


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

def get_usuarios_artistas():
    # Obtener todos los perfiles de usuarios con rol cod_rol=2
    perfiles_usuarios = PerfilUsuario.objects.filter(rol__cod_rol=2)

    for perfil in perfiles_usuarios:
        print(perfil.user.get_full_name())

    context = {
        'perfiles_usuarios': perfiles_usuarios
    }
    return context

def get_categorias():
    categorias = Categoria.objects.all()
    return categorias

@login_required
def nueva_obra(request):
    # Obtener todas las categorías
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre_obra = request.POST.get('nombre_obra')
        imagen1 = request.FILES.get('imagen1')
        imagen2 = request.FILES.get('imagen2')
        imagen3 = request.FILES.get('imagen3')
        imagen4 = request.FILES.get('imagen4')
        categoria_id = request.POST.get('categoria')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')

        # Validar que todos los campos requeridos estén presentes
        if not (nombre_obra and imagen1 and imagen2 and imagen3 and imagen4 and categoria_id and descripcion and precio):
            return HttpResponseForbidden("Todos los campos son obligatorios")

        # Obtener el estado "pendiente" (id = 2)
        estado_pendiente = EstadoObra.objects.get(cod_estado_obra=2)

        # Crear la nueva obra
        nueva_obra = Obra(
            nombre_obra=nombre_obra,
            imagen1=imagen1,
            imagen2=imagen2,
            imagen3=imagen3,
            imagen4=imagen4,
            descripcion=descripcion,
            precio=precio,
            estado=estado_pendiente,
            user=request.user,  
            categoria_id=categoria_id
        )
        nueva_obra.save()

        return redirect('perfil_usuario')  # Redireccionar a donde corresponda después de guardar

    # Pasar categorías al contexto del template si el método no es POST
    context = {'categorias': categorias}
    return render(request, 'GrupoZero/perfil_usuario.html', context)

from django.shortcuts import render
from .models import Obra, EstadoObra

def modal_obras(request):
    obras = Obra.objects.all()  
    estados = EstadoObra.objects.all() 
    context = {
        'obras': obras,
        'estados': estados,
    }
    return render(request, 'GrupoZero/perfil_admin.html', context)

def guardar_cambios_obra(request):
    if request.method == 'POST':
        obras = Obra.objects.all()  # Obtén todas las obras (ajusta según tu lógica)
        
        for obra in obras:
            estado_nuevo_id = request.POST.get(f'estado_{obra.cod_obra}')
            estado_nuevo = EstadoObra.objects.get(pk=estado_nuevo_id)
            obra.estado = estado_nuevo
            obra.save()
        
        return redirect('perfil_admin')  # Redirige a la página perfil_admin después de guardar los cambios

    # Si no es una solicitud POST, manejar aquí como desees (opcional)
    return redirect('perfil_admin')  # Redirige a la página perfil_admin en caso de no ser POST
