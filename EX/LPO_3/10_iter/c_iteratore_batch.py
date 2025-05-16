#!/opt/homebrew/bin/python3

from collections.abc import Iterator

class CIteratoreBatch(Iterator):
    """
        presa una lista, ogni volta che viene chiamata la funzione
        __next__ restituisce una lista di n elementi, decisi in
        fase di inizializzazione
        se non ci sono più elementi da restituire, li prende 
        dall'inizio
    """
    def __init__(self, lista, hop = 1):
        self._lista = lista
        self._curr_index = 0
        self._hop = hop

    
    def __next__(self):
        print("il salto è", self._hop)
        
        if self._curr_index + self._hop <= len(self._lista):
            el = self._lista[self._curr_index:(self._curr_index + self._hop)]
            self._curr_index += self._hop
            return el
        else:
            el = self._lista[self._curr_index:]
            hop = self._hop # aggiorno il salto, rimuovendo dal conto gli elementi già considerati
            self._hop = self._hop - (len(self._lista) - self._curr_index)
            self._curr_index = 0
            el = el + self.__next__()
            self._hop = hop # ripristino il salto al valore iniziale
            # questa verrà ripetuta in modo ricorsivo
            # ma è necessaria per tener conto degli oggetti già considerati
            return el

l = [1, 2, 3, 4, 5]
ogg_iter = CIteratoreBatch(l, 4)
print("seconda iterazione")
l = ogg_iter.__next__()
print(l)
print(len(l))
# prima iterazione
# il salto è 4
# [1, 2, 3, 4]
# 4

print("seconda iterazione")
l = ogg_iter.__next__()
print(l)
print(len(l))
# seconda iterazione
# il salto è 4
# il salto è 3 
# [5, 1, 2, 3]
# 4


print("terza iterazione")
l = ogg_iter.__next__()
print(l)
print(len(l))
# terza iterazione
# il salto è 4
# il salto è 2
# [4, 5, 1, 2]
# 4




