-- BASE DE DATOS: BIBLIOTECA PDF


-- =========================================
-- TABLA: Estados
-- =========================================

CREATE TABLE IF NOT EXISTS Estados (
    id_estado INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_estado TEXT NOT NULL UNIQUE
);


-- =========================================
-- TABLA: PDFs
-- =========================================

CREATE TABLE IF NOT EXISTS PDFs (
    id_pdf INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_pdf TEXT NOT NULL,
    descripcion_pdf TEXT,
    total_paginas INTEGER NOT NULL CHECK(total_paginas > 0),
    id_estado INTEGER NOT NULL,
    ruta_archivo_pdf TEXT NOT NULL UNIQUE,
    ruta_portada_pdf TEXT,

    FOREIGN KEY (id_estado)
        REFERENCES Estados(id_estado)
);


-- =========================================
-- TABLA: Grupos
-- =========================================

CREATE TABLE IF NOT EXISTS Grupos (
    id_grupo INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_grupo TEXT NOT NULL UNIQUE,
    descripcion_grupo TEXT,
    ruta_portada_grupo TEXT
);


-- =========================================
-- TABLA: Autor
-- =========================================

CREATE TABLE IF NOT EXISTS Autor (
    id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_autor TEXT NOT NULL UNIQUE
);


-- =========================================
-- TABLA: Etiquetas
-- =========================================

CREATE TABLE IF NOT EXISTS Etiquetas (
    id_etiqueta INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_etiqueta TEXT NOT NULL UNIQUE
);


-- =========================================
-- TABLA: Agrupar
-- Relación entre PDFs y Grupos
-- =========================================

CREATE TABLE IF NOT EXISTS Agrupar (
    id_pdf INTEGER NOT NULL,
    id_grupo INTEGER NOT NULL,
    fecha_agregado TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id_pdf, id_grupo),

    FOREIGN KEY (id_pdf)
        REFERENCES PDFs(id_pdf)
        ON DELETE CASCADE,

    FOREIGN KEY (id_grupo)
        REFERENCES Grupos(id_grupo)
        ON DELETE CASCADE
);


-- =========================================
-- TABLA: Crea
-- Relación entre PDFs y Autores
-- =========================================

CREATE TABLE IF NOT EXISTS Crea (
    id_pdf INTEGER NOT NULL,
    id_autor INTEGER NOT NULL,

    PRIMARY KEY (id_pdf, id_autor),

    FOREIGN KEY (id_pdf)
        REFERENCES PDFs(id_pdf)
        ON DELETE CASCADE,

    FOREIGN KEY (id_autor)
        REFERENCES Autor(id_autor)
        ON DELETE CASCADE
);


-- =========================================
-- TABLA: Tiene
-- Relación entre PDFs y Etiquetas
-- =========================================

CREATE TABLE IF NOT EXISTS Tiene (
    id_pdf INTEGER NOT NULL,
    id_etiqueta INTEGER NOT NULL,

    PRIMARY KEY (id_pdf, id_etiqueta),

    FOREIGN KEY (id_pdf)
        REFERENCES PDFs(id_pdf)
        ON DELETE CASCADE,

    FOREIGN KEY (id_etiqueta)
        REFERENCES Etiquetas(id_etiqueta)
        ON DELETE CASCADE
);


-- =========================================
-- ÍNDICES PARA CONSULTAS
-- =========================================

CREATE INDEX IF NOT EXISTS idx_pdfs_estado
ON PDFs(id_estado);

CREATE INDEX IF NOT EXISTS idx_agrupar_grupo
ON Agrupar(id_grupo);

CREATE INDEX IF NOT EXISTS idx_crea_autor
ON Crea(id_autor);

CREATE INDEX IF NOT EXISTS idx_tiene_etiqueta
ON Tiene(id_etiqueta);

-- =========================================
-- TABLA: Historial
-- =========================================

CREATE TABLE IF NOT EXISTS Historial (
    id_historial INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pdf INTEGER NOT NULL,
    fecha_apertura TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_pdf) REFERENCES PDFs(id_pdf)
        ON DELETE CASCADE
);

-- =========================================
-- TABLA: Progreso
-- =========================================

CREATE TABLE IF NOT EXISTS Progreso (
    id_pdf INTEGER PRIMARY KEY,
    pagina_actual INTEGER NOT NULL DEFAULT 1,
    fecha_actualizacion TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_pdf) REFERENCES PDFs(id_pdf)
        ON DELETE CASCADE
);
