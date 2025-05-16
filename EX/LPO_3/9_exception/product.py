#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

class CProdotto: 
    def __init__(self, idx_prodotto, prezzo):
        self.controlla_prezzo(prezzo)
        self._idx_prodotto = idx_prodotto
        self._prezzo = prezzo
    
    def controlla_prezzo(self, prezzo):
        if type(prezzo) != float:
            raise TypeError("Il prezzo deve essere un numero decimale")
        if prezzo <= 0:
            raise ValueError("Il prezzo deve essere maggiore di zero")