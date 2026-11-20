document.addEventListener("DOMContentLoaded", function () {

    console.log("Biblioteca PDF iniciada correctamente.");

    const botonCrearGrupo = document.getElementById(
        "boton_crear_grupo"
    );

    const formularioGrupo = document.getElementById(
        "formulario_grupo"
    );

    if (botonCrearGrupo && formularioGrupo) {

        botonCrearGrupo.addEventListener("click", function () {

            formularioGrupo.classList.toggle("activo");

        });

    }

});
