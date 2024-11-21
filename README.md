
# Sitio Web para Cooperativa de Artistas

Este proyecto es una página web diseñada para una cooperativa de artistas, cuyo objetivo es proporcionar una plataforma donde los artistas puedan exhibir sus obras, gestionar su perfil y controlar la visibilidad de sus creaciones. La web permite una organización clara y categorizada de las obras de arte, según el tipo de arte de cada artista.


**Funcionalidades**

* Perfil de Artista: Cada artista tiene una página donde se muestran su información personal y un listado de sus obras.
* Detalles de Obras: Al hacer clic en una obra, se accede a una página con detalles como título, descripción, precio e imagen.
* Gestión de Obras: Los artistas pueden agregar nuevas obras, subir imágenes, asignar precios y completar los detalles. Las obras deben ser aprobadas por un administrador antes de aparecer en la web.
* Autenticación y Roles: Los usuarios tienen roles específicos:
* Artista: Crea y gestiona sus obras, y edita su perfil.
* Administrador: Aprobar obras y gestionar usuarios.
* Gestión de Perfil: Los artistas pueden editar su información personal y foto de perfil, y los cambios se reflejan en su página pública.

**Mejoras Futuras**
* Categorías de Obras: Las categorías de obras estarán accesibles en la barra de navegación y representadas por imágenes interactivas en la página de inicio, las cuales serán clickeables para filtrar las obras por categoría.
* Galería de Fotos en la Página de Inicio: Se añadirá una galería de fotos en la página principal para mostrar de manera visual las obras de los artistas.
* Blog Dinámico: Las publicaciones en el "Blog" serán generadas desde las páginas de los artistas, permitiendo a cada uno crear y publicar contenido. Estas publicaciones estarán vinculadas al perfil del artista y mostrarán su foto de perfil.
## Ejecutar Localmente

1. Instala Python
Asegúrate de tener Python instalado en tu sistema. Puedes verificar esto con el siguiente comando:

        python --version
Si no tienes Python, instálalo desde python.org.


2. Clona proyecto Django

        git clone https://github.com/mariajosecq/ProyectoGZ.git
    
3. Accede al directorio del proyecto

        cd ProyectoGZ

4. Instalar dependencias

        pip install -r requirements.txt

5. Installar Pillow

        python -m pip install Pillow

6. Ejecuta el proyecto. Inicia la aplicación en un entorno de desarrollo:

        python manage.py runserver 

7. Abre el navegador utilizando la siguiente ruta:

        http://localhost:8000/GrupoZero/inicio



## Tecnologías

**Cliente:** HTML, CSS, JavaScript, jQuery

**Servidor:** Django, Django Auth

**Externos:** SQLite


## Imágenes de Referencia

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
    <img src="https://i.imgur.com/IyNP3fl.png" alt="Proyecto 1" width="400" style="border: 1px solid #ccc;"/>
    <img src="https://imgur.com/vREvF4v.png" alt="Proyecto 2" width="400" style="border: 1px solid #ccc;"/>
    <img src="https://i.imgur.com/yzk5yKh.png" alt="Proyecto 3" width="400" style="border: 1px solid #ccc;"/>
    <img src="https://imgur.com/M1KVGqv.png" alt="Proyecto 4" width="400" style="border: 1px solid #ccc;"/>
</div>



## Autores

- [María José Calderón](https://www.github.com/mariajosecq)
- [Eduardo Reyes](https://www.github.com/edreyese)
- [Felipe Urbina](https://www.github.com/michimisimo)

