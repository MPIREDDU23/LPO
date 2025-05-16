#!/opt/homebrew/bin/python3

"""
Python mette a disposizione una serie di classi
built-in
"""

ogg_lista = []
print(ogg_lista)
ogg_lista = list()
print(ogg_lista)

"""
stamperò la stessa cosa ' [] '
"""

# per estendere le classi built-in,le facciamo ereditare
# come per le classi create da noi

class CNuovaLista(list):
    pass

# questa classe eredita da list attributi e metodi

ogg_lista = CNuovaLista()
print(ogg_lista)

# possiamo aggiungere un elemento alla lista come facciamo solitamente
ogg_lista.append(1)
print(ogg_lista)

# se vogliamo modificare il comportamento di un metodo es append

class CNuovaLista(list):
    def append(self, elem):
        print("appendo l'elemento", elem)
        super().append(elem)

ogg_lista = CNuovaLista()
print(ogg_lista)
ogg_lista.append(1) # appendo l'elemento 1
ogg_lista.append(2) # appendo l'elemento 2
print(ogg_lista) # [1, 2]

