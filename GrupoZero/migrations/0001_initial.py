# Generated by Django 3.2.25 on 2024-06-11 04:21

import GrupoZero.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('cod_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('cod_rol', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=GrupoZero.models.user_directory_path)),
                ('rol', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('cod_obra', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_obra', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to=GrupoZero.models.user_directory_path)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.IntegerField()),
                ('categoria', models.ForeignKey(db_column='cod_categoria', on_delete=django.db.models.deletion.CASCADE, to='GrupoZero.categoria')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImagenObra',
            fields=[
                ('cod_imagen_obra', models.IntegerField(primary_key=True, serialize=False)),
                ('imagen_obra', models.ImageField(upload_to=GrupoZero.models.user_directory_path)),
                ('obra', models.ForeignKey(db_column='cod_obra', on_delete=django.db.models.deletion.CASCADE, to='GrupoZero.obra')),
            ],
        ),
    ]