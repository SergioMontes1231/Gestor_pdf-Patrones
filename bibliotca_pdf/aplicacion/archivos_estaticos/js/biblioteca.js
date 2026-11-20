document.addEventListener("DOMContentLoaded", () => {

    const botonImportar = document.getElementById(
        "boton_importar"
    );

    const formularioImportacion = document.getElementById(
        "formulario_importacion"
    );

    // Si los elementos no existen en esta página,
    // no realizar ninguna acción.
    if (
        !botonImportar ||
        !formularioImportacion
    ) {
        return;
    }

    botonImportar.addEventListener(
        "click",
        () => {

            formularioImportacion.classList.toggle(
                "activo"
            );

        }
    );

});
