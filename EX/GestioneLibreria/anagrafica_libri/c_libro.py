#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

class CLibro:

    def __init__(self, titolo, autore, editore, prezzo, anno_pubblicazione):

            self.titolo = titolo
            self.autore = autore
            self.editore = editore
            self.prezzo = prezzo
            self.anno_pubblicazione = anno_pubblicazione

    def _calcola_eta_libro(self, anno_corrente):
        eta_libro = anno_corrente - self.anno_pubblicazione
        return eta_libro

    def _calcola_sconto(self, anno_corrente):
        eta_libro = self._calcola_eta_libro(anno_corrente)
        if eta_libro > 5:
            sconto = self.prezzo * 5 / 100
        else:
            sconto = 0
        return sconto

    def calcola_prezzo_scontato(self, anno_corrente):
        prezzo_scontato = self.prezzo - self._calcola_sconto(anno_corrente)
        return prezzo_scontato
