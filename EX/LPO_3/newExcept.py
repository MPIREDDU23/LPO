# Tra le altre cose è anche possibile definire nuove eccezioni
#
# le eccezioni sono oggetti: 
# quando usiamo la sintaxe raise <TipoEccezione>("Messaggio")
# stiamo creando un oggetto di tipo <TipoEccezione> 
# passando al messaggio inizializzatore il msg
# e lo stiamo lanciando


# si possono definire nuove eccezioni
class CPrelievoInvalido(Exception):
    """
    eccezione personalizzata per prelievo
    """
    pass

# questa classe eredita da Exception tutto,
# possiamo quindi semplicemente sollevarla

# raise CPrelievoInvalido("Il prelievo richiesto non può essere effettuato")
# come per le altre eccezioni causa l'interruzione del programma
# e mostra il messaggio di errore a schermo

# possiamo anche personalizzarla

class CPrelievoInvalido(Exception):
    """
    eccezione personalizzata per prelievo
    """
    def __init__(self, importo_sul_conto, importo_prelevato):
        msg = "Il prelievo richiesto non può essere effettuato. "
        importo_mancante = importo_prelevato - importo_sul_conto
        msg+= "Hai cercato di prelevare " + str(importo_prelevato) + \
            " euro più di quelli presenti sul conto. "
        
        super().__init__(msg)

# raise CPrelievoInvalido(100, 150)
# CPrelievoInvalido: Il prelievo richiesto non può 
# essere effettuato. Hai cercato di prelevare 150 euro 
# più di quelli presenti sul conto. 


