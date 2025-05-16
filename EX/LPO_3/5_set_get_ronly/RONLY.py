#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

class CEsame:
    def __init__(self, codice_esame):
        self._codice_esame = self._controlla_codice(codice_esame)
    
    # possimao fare un setter per un attributo di solo lettura, 
    # altrimenti l'utente pensa che non lo sia
    # per filtrare l'input dell'utente in inizializzazione
    # utilizziamo un metodo privato
    def _controlla_codice(self, codice_esame):
        while (type(codice_esame) != str) or (len(codice_esame) != 4):
            codice_esame = input("Codice esame non valido. Reinserire[4 lettere]: ")
        return codice_esame

# se invece esiste un attributo di sola lettura
# che dipende da altri attributi, dobbiamo deinire i 
# setter e getter per gli attributi di cui dipende
# e poi definire il getter per l'attributo di sola lettura

class CEsame2:
    def __init__(self, codice_esame, voto_primo_parziale, voto_secondo_parziale):
        self._codice_esame = self._controlla_codice(codice_esame)
        self._voto_primo_parziale = voto_primo_parziale
        self._voto_secondo_parziale = voto_secondo_parziale
        # self._voto_finale = (voto_primo_parziale + voto_secondo_parziale) / 2
        # questo non è corretto, perchè se i voti vengono modificati,
        # la modifica non viene propagata al voto finale

    def calcola_voto_finale(self):
        return (self._voto_primo_parziale + self._voto_secondo_parziale) / 2
    @property
    def voto_primo_parziale(self):
        return self._voto_primo_parziale
    @voto_primo_parziale.setter
    def voto_primo_parziale(self, voto_primo_parziale):
        self._voto_primo_parziale = voto_primo_parziale
        self._voto_finale = self.calcola_voto_finale()
    @property
    def voto_secondo_parziale(self):
        return self._voto_secondo_parziale
    @voto_secondo_parziale.setter
    def voto_secondo_parziale(self, voto_secondo_parziale):
        self._voto_secondo_parziale = voto_secondo_parziale
        self._voto_finale = self.calcola_voto_finale()
        # in questo modo, quando l'utente modifica il voto
        # di uno dei due parziali, il voto finale viene
        # ricalcolato automaticamente

    
    @property
    def voto_finale(self):
        return self._voto_finale