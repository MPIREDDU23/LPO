#!/usr/bin/env python3

class CLibro():
    """
    CLibro class to represent a book in the library.
    """
    def __init__(self, id_libro, titulo, autor, editorial, anio_publicacion):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion