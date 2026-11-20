document.addEventListener("DOMContentLoaded", () => {

    const buscador = document.querySelector(
        ".buscador input"
    );

    if (!buscador) {
        return;
    }

    buscador.addEventListener(
        "input",
        () => {

            // Aquí posteriormente podremos implementar
            // búsqueda dinámica sin recargar la página.

        }
    );

});