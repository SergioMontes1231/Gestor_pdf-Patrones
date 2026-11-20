document.addEventListener("DOMContentLoaded", () => {

    const botonAnterior = document.getElementById(
        "pagina_anterior"
    );

    const botonSiguiente = document.getElementById(
        "pagina_siguiente"
    );

    const inputPagina = document.getElementById(
        "pagina_actual"
    );

    const imagenPagina = document.getElementById(
        "pagina_pdf"
    );

    let paginaActual = PAGINA_INICIAL;

    /*
    =========================================
    CAMBIAR DE PÁGINA
    =========================================
    */

    function cambiarPagina(numeroPagina) {

        // Evitar páginas fuera del documento
        if (
            numeroPagina < 1 ||
            numeroPagina > TOTAL_PAGINAS
        ) {
            return;
        }

        paginaActual = numeroPagina;

        // Actualizar el número mostrado
        inputPagina.value = paginaActual;

        // Actualizar la imagen del PDF
        imagenPagina.src =
            `/leer/${ID_PDF}/pagina/${paginaActual}`;

        // Actualizar botones
        actualizarBotones();

        // Guardar progreso
        guardarProgreso();
    }


    /*
    =========================================
    ACTUALIZAR BOTONES
    =========================================
    */

    function actualizarBotones() {

        botonAnterior.disabled =
            paginaActual <= 1;

        botonSiguiente.disabled =
            paginaActual >= TOTAL_PAGINAS;
    }


    /*
    =========================================
    GUARDAR PROGRESO
    =========================================
    */

    async function guardarProgreso() {

        const datos = new FormData();

        datos.append(
            "pagina",
            paginaActual
        );

        try {

            await fetch(
                `/leer/${ID_PDF}/progreso`,
                {
                    method: "POST",
                    body: datos
                }
            );

        } catch (error) {

            console.error(
                "Error al guardar el progreso:",
                error
            );

        }
    }


    /*
    =========================================
    BOTÓN: PÁGINA ANTERIOR
    =========================================
    */

    botonAnterior.addEventListener(
        "click",
        () => {

            cambiarPagina(
                paginaActual - 1
            );

        }
    );


    /*
    =========================================
    BOTÓN: PÁGINA SIGUIENTE
    =========================================
    */

    botonSiguiente.addEventListener(
        "click",
        () => {

            cambiarPagina(
                paginaActual + 1
            );

        }
    );


    /*
    =========================================
    ESCRIBIR NÚMERO DE PÁGINA
    =========================================
    */

    inputPagina.addEventListener(
        "change",
        () => {

            const numeroPagina = Number(
                inputPagina.value
            );

            cambiarPagina(
                numeroPagina
            );

        }
    );


    /*
    =========================================
    INICIALIZACIÓN
    =========================================
    */

    actualizarBotones();

});