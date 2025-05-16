#!/usr/bin/env python3

# l'ereditarietà multipla si può usare quando si hanno
# classi differenti con funzionalità in comune

# ricordiamo la regola DRY (Don't Repeat Yourself)
# per evitare di ripetere codice

# usiamo una classe che non esiste per essere istanziata
# ma per essere ereditata dalle classi che devono 
# fornire quelle funzionalità

# classe mixin


class CAnalisiDuplicatiMixin():
    def analisi_duplicati(self):
        trovati = {}
        duplicati = {}
        for el in self.contenitore:
            if el in trovati:
                duplicati.append(el)
            else:
                trovati[el] = 1

class CContaElementiMixin():
    def conta_elementi(self):
        n = 0
        for el in self.contenitore:
            n += 1
        return n
# la classe mixin non ha un __init__()
class CStringa(CContaElementiMixin, CAnalisiDuplicatiMixin):
    def __init__(self, stringa:str):
        self.contenitore = stringa
    
    
class CLista(CContaElementiMixin, CAnalisiDuplicatiMixin):
    def __init__(self, lista:list):
        self.contenitore = lista
    
ogg = CStringa("ciao")
print(ogg.conta_elementi()) # 4
ogg = CLista([1, 2, 3])
print(ogg.conta_elementi()) # 3


ogg = CStringa("controllare i duplicati")
print(ogg.analisi_duplicati()) # {'c': 2, 'o': 2, 'n': 2, 't': 2, 'r': 1, 'a': 1, 'l': 1, 'e': 1, 'i': 1, ' ': 1}
ogg = CLista([1, 2, 3, 1, 2])
print(ogg.analisi_duplicati()) # {1: 2, 2: 2, 3: 1}
