#!/usr/bin/env python3

class CPunto():
    def __init__(self, x):
        self.x = x


ogg = CPunto(1)
print(ogg.x) # accedo direttamente all'attributo x
ogg.x = 2 # modifico l'attributo x
print(ogg.x)


print("\nsecondo esempio")
# ora voglio proteggere l'attributo x
class CPunto():
    def __init__(self, x):
        self._x = x # l'attributo è privato
   
    def get_x(self):
        return self._x
    def set_x(self, x):
        self._x = x

ogg = CPunto(1)
print(ogg.get_x()) # accedo all'attributo x tramite il metodo get
ogg._x = 2 # modifico l'attributo x
print(ogg.get_x()) # accedo all'attributo x tramite il metodo get

'''
non è molto leggibile
'''

class CPunto():
    def __init__(self, x):
        self._x = x # l'attributo è privato
   
    # viene direttamente chiamato il metodo 
    # get_x quando si accede all'attributo x
    @property
    def x(self):
        return self._x
    
    # viene direttamente chiamato il metodo
    # set_x quando si modifica l'attributo x
    @x.setter
    def x(self, x):
        self._x = x
    
    # bisogna dichiarare prima il metodo get_x
    # e poi il metodo set_x
    # altrimenti da errore e non si può eseguire
    # non può esistere il setter senza il getter
print("\nterzo esempio")
ogg = CPunto(1)
print(ogg.x) # accedo all'attributo x tramite il metodo get
ogg.x = 2 # modifico l'attributo x tramite il metodo set
print(ogg.x) # accedo all'attributo x tramite il metodo get


# i getter e setter sono metodi che permettono di 
# accedere e modificare gli attributi privati, sono 
# utili per "proteggere gli attributi" magari per 
# filtrare i dati in ingresso o in uscita


class CStudenteSuperiori():
    def __init__(self, cognome, anno_frequenza):
        self._cognome = cognome
        self._anno_frequenza = anno_frequenza
    
    @property
    def cognome(self):
        return self._cognome
    
    @property
    def anno_frequenza(self):
        return self._anno_frequenza
    # si può usare il setter per filtrare i dati in ingresso
    # in questo caso l'anno di frequenza deve essere intero e
    # compreso tra 1 e 5
    @anno_frequenza.setter
    def anno_frequenza(self, anno_frequenza: int):
        if anno_frequenza < 1 or anno_frequenza > 5:
            raise ValueError("anno di frequenza non valido")
        self._anno_frequenza = anno_frequenza
    

ogg = CStudenteSuperiori("Rossi", 3)
print(ogg.cognome)
print(ogg.anno_frequenza)
# ogg.cognome = "Verdi" # non posso modificare il cognome
# si può modificare accedendo direttamente all'attributo
ogg._cognome = "Verdi" # così funziona, ma non è buona pratica
# se l'attributo è privato, modificarlo manualmente potrebbe compromettere
# il funzionamento della classe
print(ogg._cognome) # accedo direttamente all'attributo cognome
# sempre meglio usare i metodi get e set




