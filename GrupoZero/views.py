from django.shortcuts import render

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