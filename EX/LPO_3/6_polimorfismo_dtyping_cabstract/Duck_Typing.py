#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

# If it walks like a duck and quacks like a duck, it is a duck
# In python, se devo definire delle classi diverse che funzionano in 
# modo diverso in base al tipo di oggetto che sono, posso definire la medesima
# interfaccia anche se non ereditano dalla stessa classe
# In questo caso, non ho bisogno di definire una classe madre

class CQuaderno:
    prezzo = 10
    
    @classmethod
    def getPrezzo(cls):
        return cls.prezzo*0.90 # applica uno sconto del 10% al prezzo

class CTazza:
    prezzo = 5
    
    @classmethod
    def getPrezzo(cls):
        return cls.prezzo - 1 # rimuove 1 euro dal prezzo   
    
# nasce un problema, se un altro programmatore vuole aiutarci a deffinire altre classi:
# a quel punto non saprà he interfaccia usare
# definiamo una classe Astratta

from abc import ABC, abstractmethod # importo le librerie necessarie

class CProdotto(ABC): # definisco la classe astratta

    @classmethod
    @abstractmethod
    def getPrezzo(cls): # definisco il metodo astratto
        pass # non implemento nulla

# se definisco una classe che non implementa il metodo astratto, mi da errore
class CQuadro(CProdotto): # definisco la classe che estende la classe astratta
    pass

# ogg = CQuadro() # creo un oggetto della classe CQuadro, 
# la console dice: TypeError: Can't instantiate abstract class CQuadro with abstract method getPrezzo
