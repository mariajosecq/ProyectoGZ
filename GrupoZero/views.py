from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
        # Verifica si se está realizando un registro o un inicio de sesión
        if 'registro' in request.POST:
            # Registro de nuevo usuario
            email = request.POST.get('email_registro')
            username = request.POST.get('nombre_registro')
            password = request.POST.get('contrasena_registro')
            user = User.objects.create_user(username=username, email=email, password=password)
            # Redirige al usuario a la página de éxito después del registro
            return redirect('pagina_exito')
        elif 'inicio_sesion' in request.POST:
            # Inicio de sesión de usuario existente
            email = request.POST.get('email_inicio_sesion')
            password = request.POST.get('contrasena_inicio_sesion')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Redirige al usuario a la página de éxito después del inicio de sesión
                return redirect('pagina_exito')
            else:
                # El inicio de sesión falló, puedes agregar un mensaje de error
                # y renderizar nuevamente el formulario de inicio de sesión
                return render(request, 'GrupoZero/base.html', {'error': 'Inicio de sesión fallido'})
    
    # Si el método no es POST, simplemente renderiza el formulario
    return render(request, 'GrupoZero/base.html')