# from anagrafica_libri.c_libro import CLibro
from .c_libro import CLibro  # import relativo
"""
Il primo è un import assoluto, il secondo è un import relativo.
Un import assoluto è un import che parte dalla radice del package.
in questo caso parte da GESTIONE_LIBRERIA.


"""

class CListaLibri:

    def __init__(self):
        self._lista = []

    def _crea_nuovo_oggetto_libro(self):
        # acquisisci i dati
        titolo = input("inserisci il titolo del libro ")
        autore = input("inserisci l'autore del libro ")
        editore = input("inserisci l'editore del libro ")
        prezzo = float(input("inserisci il prezzo del libro "))
        anno_pubblicazione = int(
            input("inserisci l'anno di pubblicazione del libro "))

        # crea un oggetto appartenente alla classe CLibro
        oggetto_libro = CLibro(titolo, autore, editore, prezzo,
                               anno_pubblicazione)
        return oggetto_libro

    def aggiungi_libro(self):
        # acquisisce i dati di un nuovo libro e crea un oggetto di tipo CLibro
        oggetto_libro = self._crea_nuovo_oggetto_libro()
        self._lista = self._lista + [oggetto_libro]

    def mostra_prezzo_libro(self, titolo, anno_corrente):

        oggetto_libro = self._cerca_libro(titolo)
        print(oggetto_libro.calcola_prezzo_scontato(anno_corrente))

    def _cerca_libro(self, titolo):
        for libro in self._lista:
            if libro.titolo == titolo:
                return libro
        print("Libro non trovato!")


