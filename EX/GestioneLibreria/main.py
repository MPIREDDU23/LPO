#!/opt/homebrew/bin/python3

"""
Questo script serve per mostrare che è possibile utilizzare oggetti definiti in
packages differenti.
"""
from anagrafica_libri.c_lista_libri import *
from anagrafica_clienti.c_azienda import *

# queste importo sono pericolose, perché se sono presenti
# classi con lo stesso nome si possono creare
# comportamenti inasttesi


oggetto_cliente = CAzienda("12345678901", "123", "070998899")
print("La partita iva e' ", oggetto_cliente.partita_iva)
print("Il numero di telefono e' ", oggetto_cliente.numero_telefono)

lista_libri = CListaLibri()
lista_libri.aggiungi_libro()

