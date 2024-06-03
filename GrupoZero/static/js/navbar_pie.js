const header = document.querySelector('header');

header.innerHTML = `
   <nav class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
       <div class="container-fluid d-flex justify-content-between align-items-center">
           <!--Logo-->
           <a href="principal.html">
               <img class="img-logo" src="{% static 'img/img-principal/logo-blanco.png' %}" alt="LOGO">
           </a>
           <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
               <span class="navbar-toggler-icon"></span>
           </button>

           <div>
                <button type="button" class="navbar-blog btn-outline-light">
                    <a href="blog.html" class="btn-link">BLOG</a>
                </button>    
           </div>

           <!--Desplegables-->
           <div class="collapse navbar-collapse" id="navbarNav">
               <ul class="navbar-nav">
                   <li class="nav-item dropdown">
                       <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                           Categoría
                       </a>
                       <ul class="dropdown-menu">
                           <li><a class="dropdown-item" href="#">Pintura</a></li>
                           <li><a class="dropdown-item" href="#">Escultura</a></li>
                           <li><a class="dropdown-item" href="#">Tejido</a></li>
                           <li><a class="dropdown-item" href="#">Orfebrería</a></li>
                           <li><a class="dropdown-item" href="#">Otros</a></li>
                       </ul>
                   </li>
                   <li class="nav-item dropdown">
                       <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                           Artistas
                       </a>
                       <ul class="dropdown-menu">
                           <li><a class="dropdown-item" href="detalle_autor.html">Daniela Fernández</a></li>
                           <li><a class="dropdown-item" href="detalle_autor2.html">Gabriel Marín</a></li>                                
                           <li><a class="dropdown-item" href="detalle_autor3.html">Sergio Roger</a></li>
                       </ul>
                   </li>
               </ul>
           </div>
           <!--Buscador-->
           <form class="d-flex busqueda" role="search">
               <input class="form-control me-2" type="search" placeholder="Buscar" aria-label="Search">
               <button class="btn btn-outline-light" type="submit">Buscar</button>
           </form>
           <!-- Botón de Iniciar Sesión -->
           
           <div class="login">
               <button type="button" class="navbar-login btn btn-outline-light" id="mostrar-login">INICIAR SESION</button>
           </div>
       </div>
   </nav>
`;

const footer = document.querySelector('footer');
footer.innerHTML = `
    <div class="pie">
        <div class="imagenPie">
            <img src="img/img-principal/logo-blanco.png" alt="logo">
        </div>
        <div class="textoPie">
            <u><b><h5>Contacto</h5></u></b>
            <p>Fono:9999999999</p>

            <!--Modal para enviar correo con API-->
            <!--Botón correo-->
            <button type="button" class="boton-correo" data-bs-toggle="modal" data-bs-target="#ModalCorreo">
                <b>info@grupozero.com</b>
            </button>
            <!Modal-->
            <div class="modal" tabindex="-1" id="ModalCorreo">
                <div class="modal-dialog modal-s">
                    <div class="modal-content">
                        <div class="modal-header fuente-titulo-blanco">
                            <h5 class="modal-title">ENVIAR CORREO</h5>
                        </div>
                        <div class="modal-body fuente-parrafo-negro">
                            <!-- Forulario -->
                            <form id="CorreoForm">
                                <div class="mb-4">
                                    <label for="FormControlNombre" class="form-label">Nombre</label>
                                    <textarea class="form-control" id="FormControlNombre" rows="1"></textarea>
                                </div>
                                <div class="mb-4">
                                    <label for="email">Correo:</label>
                                    <input type="email" id="emailapi" name="email" class="form-control fuente-parrafo-negro">
                                </div>
                                <div class="mb-4">
                                    <label for="FormControlMensaje" class="form-label">Mensaje</label>
                                    <textarea class="form-control fuente-parrafo-negro" id="FormControlMensaje" rows="5"></textarea>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                                    <!-- Ensure this button is of type submit -->
                                    <button type="submit" class="btn boton-modal">Enviar correo</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
`;

const iniciarSesion = document.querySelector('formIniciarSesion');
iniciarSesion.innerHTML = `
<!--Formulario para iniciar sesion y Crear cuenta-->
<form class="form" novalidate>
    <div class="tab-header">
        <div class="active">Crear Cuenta</div>
        <div>Iniciar Sesion</div>
    </div>
    <div class="tab-cont">
        <div class="tab-body active">
            <div class="form-ele">
                <input type="email" placeholder="Email" class="newmail">
            </div>
            <div class="form-ele">
                <input type="text" placeholder="Nombre" class="newname">
            </div>
            <div class="form-ele">
                <input type="password" placeholder="Contraseña" class="newpass">
            </div>
            <div class="form-ele">
                <button type="submit" class="btn-crear">Crear Cuenta</button>
            </div>
            <div class="form-ele">
                <div class="cerrar-login">&times;</div>
            </div>
        </div>
        <div class="tab-body" dir="tab-body-accs">
            <div class="form-ele">
                <input type="email" placeholder="Email" class="email">
            </div>
            <div class=" form-ele">
                <input type="password" placeholder="Contraseña" class="pass">
            </div>
            <div class="form-ele">
                <input type="checkbox" id="recordar">
                <label for="recordarme">Recordarme</label>
            </div>
            <div class="form-ele">
                <button type="submit" class="btn-acceder">Ingresar</button>
            </div>
            <div class="form-ele">
                <a href="#">
                    <center>¿Olvidaste tu contraseña?</center>
                </a>
            </div>
            <div class="form-ele">
                <div class="cerrar-login">&times;</div>
            </div>
        </div>
    </div>
</form>
`;

// Abrir, cerrar y cambiar el login
document.addEventListener("DOMContentLoaded", function () {
    let tabpanes = document.getElementsByClassName("tab-header")[0].getElementsByTagName("div");

    //abrir, cerrar y cambiar el login
    for (let i = 0; i < tabpanes.length; i++) {
        tabpanes[i].addEventListener("click", function () {

            document.getElementsByClassName("tab-header")[0].getElementsByClassName("active")[0].classList.remove("active");

            tabpanes[i].classList.add("active");

            document.getElementsByClassName("tab-cont")[0].getElementsByClassName("tab-body active")[0].classList.remove("active");

            document.getElementsByClassName("tab-cont")[0].getElementsByClassName("tab-body")[i].classList.add("active");
        });
    }

    document.querySelector("#mostrar-login").addEventListener("click", function () {
        console.log("Botón 'Iniciar sesión' clicado.");
        document.querySelector(".form").classList.add("open");
    });

    document.querySelector(".form .tab-cont .cerrar-login").addEventListener("click", function () {
        console.log("Botón 'Cerrar sesión' clicado.");
        document.querySelector(".form").classList.remove("open");
    });

    document.querySelector(".form .tab-cont .tab-body:nth-child(2) .cerrar-login").addEventListener("click", function () {
        document.querySelector(".form").classList.remove("open");
    });


    // Validacion de formulario

    // Evitar envío de formulario por defecto
    document.querySelector(".form").addEventListener("submit", function (event) {
        event.preventDefault();
    });

    // Validación del formulario de Crear Cuenta
    const formCrearCuenta = document.querySelector('.tab-body.active');
    const btnCrearCuenta = formCrearCuenta.querySelector('.btn-crear');
    const inputFieldsCrearCuenta = formCrearCuenta.querySelectorAll('input');
    inputFieldsCrearCuenta.forEach(input => {
        input.addEventListener('input', function () {
            input.classList.remove('placeholder-red');
        });
    });
    inputFieldsCrearCuenta.forEach(input => {
        input.addEventListener('blur', function () {
            validateField(input);
        });
    });
    btnCrearCuenta.addEventListener('click', function (event) {
        event.preventDefault();
        console.log('Botón "Crear Cuenta" clicado');
        const emailFieldCrearCuenta = formCrearCuenta.querySelector('.newmail');
        const nameFieldCrearCuenta = formCrearCuenta.querySelector('.newname');
        const passFieldCrearCuenta = formCrearCuenta.querySelector('.newpass');
        validateAndSubmitForm(emailFieldCrearCuenta, nameFieldCrearCuenta, passFieldCrearCuenta, formCrearCuenta);
    });

    // Validación del formulario de Acceder
    const formAcceder = document.querySelector('.tab-body[dir="tab-body-accs"]');
    const btnAcceder = formAcceder.querySelector('.btn-acceder');
    const inputFieldsAcceder = formAcceder.querySelectorAll('input');
    inputFieldsAcceder.forEach(input => {
        input.addEventListener('input', function () {
            input.classList.remove('placeholder-red');
        });
    });
    inputFieldsAcceder.forEach(input => {
        input.addEventListener('blur', function () {
            validateField(input);
        });
    });
    btnAcceder.addEventListener('click', function (event) {
        event.preventDefault();
        console.log('Botón "Acceder" clicado');
        const emailFieldAcceder = formAcceder.querySelector('.email');
        const passFieldAcceder = formAcceder.querySelector('.pass');
        validateAndSubmitForm(emailFieldAcceder, null, passFieldAcceder, formAcceder);
    });

    // Función para validar y enviar el formulario
    function validateAndSubmitForm(emailField, nameField, passField, form) {
        const emailValue = emailField.value.trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const passValue = passField.value.trim();

        if (!emailValue || !emailRegex.test(emailValue)) {
            emailField.classList.remove('valid');
            emailField.classList.add('invalid');
            emailField.value = '';
            emailField.placeholder = 'Email inválido';
            emailField.classList.add('placeholder-red');
        } else {
            emailField.classList.remove('invalid');
            emailField.classList.add('valid');
            emailField.placeholder = '';
            emailField.classList.remove('placeholder-red');
            console.log('Campo de email válido');
        }

        if (nameField && (nameField.value.trim().length < 4)) {
            nameField.classList.remove('valid');
            nameField.classList.add('invalid');
            nameField.value = '';
            nameField.placeholder = 'Nombre inválido (mín. 4 caracteres)';
            nameField.classList.add('placeholder-red');
        } else if (nameField) {
            nameField.classList.remove('invalid');
            nameField.classList.add('valid');
            nameField.placeholder = '';
            nameField.classList.remove('placeholder-red');
            console.log('Campo de nombre válido');
        }

        if (!passValue || passValue.length < 8) {
            passField.classList.remove('valid');
            passField.classList.add('invalid');
            passField.value = '';
            passField.placeholder = 'Contraseña inválida (mín. 8 caracteres)';
            passField.classList.add('placeholder-red');
        } else {
            passField.classList.remove('invalid');
            passField.classList.add('valid');
            passField.placeholder = '';
            passField.classList.remove('placeholder-red');
            console.log('Campo de contraseña válido');
        }

        if (emailField.classList.contains('valid') && (nameField ? nameField.classList.contains('valid') : true) && passField.classList.contains('valid')) {
            console.log('Todos los campos son válidos, enviando formulario');
            form.submit();
        } else {
            console.log('Hay campos inválidos, el formulario no se enviará.');
        }
    }

    // Función para validar el campo después de blur
    function validateField(input) {
        if (input.value.trim()) {
            input.classList.add('valid');
            input.classList.remove('invalid');
            console.log('Campo válido después de blur:', input.className);
        } else {
            input.classList.add('invalid');
            input.classList.remove('valid');
            console.log('Campo inválido después de blur:', input.className);
        }
    }
});