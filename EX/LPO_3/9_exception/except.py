#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

"""
    Durante l'esecuzione di un programma, possono verificarsi errori
    imprevisti che interrompono il normale flusso di esecuzione.

    Dovuti ad esempio ad input dell'utente o risultati che 
    siano invalidi o imprevisti. (n / 0)
    Questi eventi generano eccezioni
"""

# x = 5 / 0 # ZeroDivisionError: division by zero

lista = [1, 2, 3]
# print(lista[3]) # IndexError: list index out of range

# a = 5 + [3] # TypeError: unsupported operand type(s) for +: 'int' and 'list'

# possiamo anche decidere di sollevare noi stessi le eccezioni
# raise <TipoEccezione>("Messaggio")

# eccezioni più comuni
    # ValueError
    # TypeError
    # NotImplementedError

class CEsame:
    def __init__(self, voto, nome):
        self._nome = nome
        self._voto = voto

    @property
    def voto(self):
        return self._voto
    
    @property
    def nome(self):
        return self._nome
    
"""
    Ad esempio, se vogliamo che il voto sia compreso tra 0 e 30
    oppure che sia un numero intero, 

    possiamo usare type(<object>) per controllare il tipo
"""

if type(30) == int:
    print("è un intero")
else:
    print("non è un intero")

# modifichiamo la classe CEsame
class CEsame:
    def __init__(self, voto, nome):
        self.controllo_voto(voto)
        self._nome = nome
        self._voto = voto
    
    @property
    def voto(self):
        return self._voto
    
    @property
    def nome(self):
        return self._nome
    
    def controllo_voto(self, voto):
        if type(voto) != int:
            raise TypeError("Il voto deve essere un numero intero")
        if voto < 0 or voto > 30:
            raise ValueError("Il voto deve essere compreso tra zero e 30")

# esempio di utilizzo
esame = CEsame(30, "Matematica")
print(esame.voto)  # Output: 30
# esame = CEsame(31, "Matematica")  # ValueError: Il voto deve essere compreso tra 0 e 30
# esame = CEsame("30", "Matematica")  # TypeError: Il voto deve essere un numero intero

# non si può semplicemente stampare i messaggi di errore, perché 
    # il programma continuerebbe a generare risultati errati
    # l'utente potrebbe non vedere il messaggio di errore

    # le eccezioni permettono di terminare il programma
    # liberando le risorse e segnalando la causa dell'interruzione *
    # fornisce messaggiu più informativi

    # * I calcoli vengono eseguiti in GPU e occupare inutilmente
    # * memoria è uno spreco di risorse

# le eccezioni possono essere gestite
# con le istruzioni try e except
"""
    try:
        ...(codice da eseguire se l'esito non genera eccezioni)...
    except Exception:
        ...(codice da eseguire se un'eccezione qualsiasi si verifica)...
"""

# si possono gestire anche eccezioni specifiche
"""
    try:
        ...(codice da eseguire se l'esito non genera eccezioni)...
    except <TipoEccezione>:
        ...(codice da eseguire se si verifica l'eccezione specificata)...

"""

# anche diverse eccezioni possono essere gestite

"""
    try:
        ...(codice da eseguire se l'esito non genera eccezioni)...
    except (<TipoEccezione1>, <TipoEccezione2>):
        ...(codice da eseguire se si verifica l'eccezione specificata)...
    except <TipoEccezione3>:
        ...(codice da eseguire se si verifica l'eccezione specificata)...
"""

class CStatisticheAcuquisti:
    def __init__(self, lista_prezzi):
        self._lista_prezzi = lista_prezzi

    def calcola_prezzo_medio(self):
        tot = 0
        for prezzo in self._lista_prezzi:
            tot += prezzo
        return tot / len(self._lista_prezzi)
    
    def stampa_prezzo_medio(self):
        try:
            prezzo_medio = self.calcola_prezzo_medio()
            print("Il prezzo medio è:", prezzo_medio)
        except Exception: 
            print("Non posso calcolare il prezzo per questa lista")

# si potrebbe fare in modo che calcola_prezzo_medio
# si occupasse di gestire le eccezioni
# ma non è una buona pratica, è meglio che sia il metodo
# che lo chiama a gestirle


class CScontrino:
    def __init__(self, lista_prezzi):
        self._lista_prezzi = lista_prezzi
    
    def calcola_prezzo_totale(self):
        tot = 0
        try:
            for prezzo in self._lista_prezzi:
                tot += prezzo
        except TypeError:
            print("Non posso calcolare il prezzo perché uno o pi" \
            "ù  prezzi sono invalidi")
            return None
        return tot
    
    # se  al posto di un numero, viene inserito un carattere
    # viene sollevata un'eccezione TypeError


