# __init__ viene chiamato quando creo un oggetto e 
# lo inizializzo


class COggetto:
    def __init__(self, nome, colore):
        self.nome = nome
        self.colore = colore
    # questo metodo viene chiamato 'costruttore'
    # 2 cose in contrasto:
    # 1. __init__ riceve l'istanza come primo argomento
    # 2. __init__ non restituisce niente

    # in realtà __new__ è il costruttore, che 
    # si occupa di creare l'oggetto

# tutte le classi ereditano da object
# class COggetto(object):

# questa classe implementa dei metodi che vengono ereditati
# dalle altre classi
# __new__ è tra quelli

'''
    Viene prima invocato prima il metodo __new__ che crea 
    (costruisce) lʼoggetto. 
    Se restituisce unʼistanza di classe (come di default) 
    viene poi invocato il metodo 
    __init__ che inizializza lʼoggetto (setta i valori degli 
    attributi).
    Quindi in realtà:
        -__init__ è chiamato impropriamente “costruttore”
        -in realtà il metodo “costruttore” è il metodo __new__
'''

""" 
    prima viene chiamato __new__ che crea l'oggetto
    poi viene chiamato __init__ che inizializza l'oggetto
"""

"""
    Le classi ereditano da object sia __new__ che __init__
    infatti non è necessario definirli
"""

class COggetto:
    @staticmethod
    def stampa():
        print("ciao")

ogg = COggetto()
ogg.stampa()