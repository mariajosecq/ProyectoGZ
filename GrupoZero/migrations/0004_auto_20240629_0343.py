# Generated by Django 3.2.25 on 2024-06-29 07:43

import GrupoZero.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrupoZero', '0003_alter_perfilusuario_rol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obra',
            old_name='imagen',
            new_name='imagen1',
        ),
        migrations.AddField(
            model_name='obra',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to=GrupoZero.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='obra',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to=GrupoZero.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='obra',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to=GrupoZero.models.user_directory_path),
        ),
    ]
