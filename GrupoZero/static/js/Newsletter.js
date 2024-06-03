const formNewsLetter = document.querySelector('.formNewsLetter');
formNewsLetter.innerHTML = `
<div class="formNewsLetter cerrarform">
<div class="imagen"></div>
<form id="form" novalidate class="formulario">
    <div class="cerrar"><a href="">x</a></div>
    <h3>Ingresa tus datos y <br> mantente informado</h3>
    <div class="newsletterinput">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" placeholder=" Ingrese su nombre">
    </div>
    <div class="newsletterinput">
        <label for="apellido">Apellido:</label>
        <input type="text" id="apellido" placeholder=" Ingrese su apellido">
    </div>
    <div class="newsletterinput">
        <label for="email">Email:</label>
        <input type="email" id="email" placeholder=" Ingrese su email">
    </div>
    <div class="newsletterinput">
        <button type="submit" id="btn-acceder">Unirse</button>
    </div>
</form>
</div>
`;

if (window.location.pathname === "/blog.html") {
    // Ocultar el popover
    document.querySelector(".avisoNewsLetter").style.display = "none";
}else{
    const popOver = document.querySelector('.avisoNewsLetter');
    popOver.innerHTML = `
    <div class="aviso">
        <div class="espacio">
            <button class="newsletter">Únete a nuestro newsletter</button>
            <div class="cerrar"><a href="">x</a></div>
        </div>
    </div>
    `;

document.addEventListener("DOMContentLoaded", function () {

    // abrir el formulario
    document.querySelectorAll(".boton-unirse, .newsletter").forEach(function (button) {
        button.addEventListener("click", function () {
            console.log("botón de newsletter clicado.");
            document.querySelector(".formNewsLetter .cerrarform").classList.remove("cerrarform");
        });
    });

    // cerrar el formulario
    document.querySelector(".formulario .cerrar a").addEventListener("click", function (event) {
        event.preventDefault();
        console.log("botón cerrar newsletter clicado.");
        document.querySelector(".formNewsLetter").classList.add("cerrarform");
    });

    // cerrar el popOver
    document.querySelector(".aviso .cerrar a").addEventListener("click", function (event) {
        event.preventDefault();
        console.log("botón cerrar popOver clicado.");
        document.querySelector(".aviso").classList.add("cerrarform");
    });  

    //validacion de formulario
    const form = document.getElementById("form");
    const nombre = document.getElementById("nombre");
    const apellido = document.getElementById("apellido");
    const email = document.getElementById("email");

    function validarEmail(mail) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(mail);
    }

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        console.log("revisando formulario");

        let a = 0;

        if (nombre.value.length < 4) {
            nombre.classList.remove("verde");
            nombre.classList.add("rojo");
            nombre.value = "";
            nombre.placeholder = 'nombre muy corto (min. 4 caracteres)';
            a += 1;
            console.log("nombre no válido");
        } else {
            nombre.classList.remove("rojo");
            nombre.classList.add("verde");
            console.log("nombre válido");
        }

        if (apellido.value.length < 4) {
            apellido.classList.remove("verde");
            apellido.classList.add("rojo");
            apellido.value = "";
            apellido.placeholder = 'apellido muy corto (min. 4 caracteres)';
            a += 1;
            console.log("apellido no válido");
        } else {
            apellido.classList.remove("rojo");
            apellido.classList.add("verde");
            console.log("apellido válido");
        }

        if (!validarEmail(email.value)) {
            email.classList.remove("verde");
            email.classList.add("rojo");
            email.value = "";
            email.placeholder = 'formato de email no válido';
            a += 1;
            console.log("email no válido");
        } else {
            email.classList.remove("rojo");
            email.classList.add("verde");
            console.log("email válido");
        }

        if (a === 0) {
            form.submit();
            console.log("formulario enviado con éxito");
        }
    });
});
}