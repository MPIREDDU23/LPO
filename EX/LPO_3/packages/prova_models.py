#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

from models.clibro import CLibro
# si può fare anche import *
# ma è sconsigliato perché non si sa cosa si importa
# si potrebbe importare una classe con lo stesso nome di una già esistente
# e quindi si andrebbe a sovrascrivere, portando un comportamento inatteso


id = 1
titolo = "El Principito"
author = "Antoine de Saint-Exupéry"
editorial = "Reynal & Hitchcock"
anno_pub = 1943
libro = CLibro(id, titolo, author, editorial, anno_pub)
print(libro.id_libro)  # Output: 1
print(libro.titulo)  # Output: El Principito
print(libro.autor)  # Output: Antoine de Saint-Exupéry
print(libro.editorial)  # Output: Reynal & Hitchcock
print(libro.anio_publicacion)  # Output: 1943


