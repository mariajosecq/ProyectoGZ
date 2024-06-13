from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    imagen = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    rol = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.user.id)

class Rol(models.Model):
    cod_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=20)

    def __str__(self):
        return str(self.cod_rol)
    
class Categoria(models.Model):
    cod_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=20)

    def __self__(self):
        return str(self.cod_categoria)
    
class Obra(models.Model):
    cod_obra = models.IntegerField(primary_key=True)
    nombre_obra = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to=user_directory_path)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')
    categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, to_field='cod_categoria', db_column='cod_categoria')


    def __str__(self):
        return str(self.cod_obra)
    
class ImagenObra(models.Model):
    cod_imagen_obra = models.IntegerField(primary_key=True)
    imagen_obra = models.ImageField(upload_to=user_directory_path)
    obra = models.ForeignKey('Obra',on_delete=models.CASCADE, to_field='cod_obra', db_column='cod_obra')
    
    def __str__(self):
        return str(self.cod_imagen_obra)
