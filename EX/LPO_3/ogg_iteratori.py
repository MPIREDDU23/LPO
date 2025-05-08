# oggetti iteratori
# oggetti iterabili

# Esempio:
# Abbiamo una lista e vogliamo una funzione che ad ogni chiamata
# restituisca il prossimo elemento della lista
# partendo dal primo elemento

# costruiamo un oggetto iterarore

# In Python si utilizza la funzione built-in next

# es abbiamo la classe CIteratore2Elementi

"""
    l = [1, 2, 3, 4, 5]
    ogg_iter = CIteratore2Elementi(l)
    for i in range(10)
        print(next(ogg_iter))
    # stampa
    [1, 2]
    [3, 4]
    StopIteration
"""

# esiste la classe astratta chiamata Iterator
# che definisce l'interfaccia per gli oggetti iteratori

from collections.abc import Iterator

class CProvaIteratore(Iterator):
    pass

# ogg_iter = CProvaIteratore()
# TypeError: Can't instantiate abstract class 
# CProvaIteratore without an implementation for 
# abstract method '__next__'

# dobbiamo implementare il metodo __next__ 

    # deve implementare il recupero degli n elementi
    # dell'oggetto e generare un'eccezione StopIteration
    # quando vogliamo che non restituisca più nulla



class CIteratore2Elementi(Iterator):
    def __init__(self, lista):
        self._lista = lista
        self._curr_index = 0
    
    def __next__(self):
        if self._curr_index + 2 <= len(self._lista):
            el = self._lista[self._curr_index:self._curr_index+2]
            self._curr_index += 2
            return el
        else:
            raise StopIteration
    

