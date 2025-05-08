"""
    L'istruzione iterativa for può essere utilizzata con istanze
    di diverde classi: 
        - liste
        - tuple
        - dizionari
        - stringhe
    Non si può utilizzare su un'oggetto qualsiasi
"""
class CNuovaLista():
    def __init__(self, lista):
        self._lista = lista
    
l = CNuovaLista([1, 2, 3, 4, 5])
# for i in l:
#     print(i)
# TypeError: 'CNuovaLista' object is not iterable

"""
    Può essere utilizzata su un oggetto iterabile
    che sono oggetti che implementano il protocollo di iterazione
    definendo un metodo __iter__ e un metodo che restituisce
    un oggetto iteratore

    L'oggetto viene utilizzato dal for per recuperare gli elementi
    dell'oggetto iterabile
"""

from ogg_iteratori import CIteratore2Elementi

class CNuovaLista():
    def __init__(self, lista):
        self._lista = lista
    
    def __iter__(self):
        return CIteratore2Elementi(self._lista)

l = [1, 2, 3, 4, 5]
ogg = CNuovaLista(l)


ogg_iteratore = iter(ogg) # restutuisce un oggetto iteratore, se la classe imple1menta il metodo __iter__
print(ogg_iteratore) # stampa: <ogg_iteratori.CIteratore2Elementi object at 0x102384d70>

# le strutture built-in di Python sono iterabili
# quindi implementano il metodo __iter__

l = [1, 2, 3, 4, 5]
ogg_iteratore = iter(l) # restutisce un oggetto iteratore
print(ogg_iteratore) # stampa: <list_iterator object at 0x102384d70>


print(next(ogg_iteratore)) # stampa: 1

"""
    se implementiamo il metodo __iter__ in una classe
    possiamo utilizzare l'oggetto in un ciclo for
"""
l = [1, 2, 3, 4, 5]
ogg = CNuovaLista(l)
for i in ogg:
    print(i) # stampa: 1 2 3 4 5

"""
    Le classi di oggetti Iterabili e Iteratori sono forniscono un buon 
    esempio di utilizzo di diversi concetti visti a lezione quali:
        -duck typing
        -utilizzo di classi astratte
        -utilizzo delle eccezioni
"""

