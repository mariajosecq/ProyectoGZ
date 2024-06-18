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
    const btnCrearCuenta = document.querySelector('.btn-crear');
    
    btnCrearCuenta.addEventListener('click', function (event) {
        event.preventDefault();
        console.log('Botón "Crear Cuenta" clicado');

        // Encontrar el formulario padre del botón clicado
        const formCrearCuenta = this.closest('form');

        const emailFieldCrearCuenta = formCrearCuenta.querySelector('.newmail');
        const nameFieldCrearCuenta = formCrearCuenta.querySelector('.newname');
        const passFieldCrearCuenta = formCrearCuenta.querySelector('.newpass');

        // Agregar eventos de input y blur solo para los campos de este formulario
        const inputFieldsCrearCuenta = formCrearCuenta.querySelectorAll('input');
        inputFieldsCrearCuenta.forEach(input => {
            input.addEventListener('input', function () {
                input.classList.remove('placeholder-red');
            });
            input.addEventListener('blur', function () {
                validateField(input);
            });
        });

        validateAndSubmitForm(emailFieldCrearCuenta, nameFieldCrearCuenta, passFieldCrearCuenta, formCrearCuenta);
    });

    // Validación del formulario de Acceder
    const btnAcceder = document.querySelector('.btn-acceder');
    
    btnAcceder.addEventListener('click', function (event) {
        event.preventDefault();
        console.log('Botón "Acceder" clicado');

        // Encontrar el formulario padre del botón clicado
        const formAcceder = this.closest('form');

        const emailFieldAcceder = formAcceder.querySelector('.email');
        const passFieldAcceder = formAcceder.querySelector('.pass');

        // Agregar eventos de input y blur solo para los campos de este formulario
        const inputFieldsAcceder = formAcceder.querySelectorAll('input');
        inputFieldsAcceder.forEach(input => {
            input.addEventListener('input', function () {
                input.classList.remove('placeholder-red');
            });
            input.addEventListener('blur', function () {
                validateField(input);
            });
        });

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
            console.log(form);
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

function setAccion(accion) {
    document.getElementById('accion').value = accion;
}
