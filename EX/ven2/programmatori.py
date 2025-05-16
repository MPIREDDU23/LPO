#!/opt/homebrew/bin/python3

# mi serve una classe programmatore, una sotto classe junior e una sotto classe senior
# la classe programmatore ha un attributo nome, uno cognome e uno stipendio (di 1500 euro)
# la classe junior ha un attributo bonus di 500 euro
# la classe senior ha un attributo bonus di 1000 euro
# la classe programmatore ha un metodo crea_oggetto_programmatore che chiede all'utente di inserire nome, cognome e stipendio

#alla classe junior aggiungere un metodo pubblico chiamato info che stampi : "I programmatori Junior sono programmatori con meno di 5 anni di esperienza"
#alla classe senior aggiungere un metodo pubblico chiamato info che stampi : "I programmatori Senior sono programmatori con piu' di 5 anni di esperienza"

class CProgrammatore:
    def __init__(self, nome, cognome, stipendio = 1500):
        self.nome = nome
        self.cognome = cognome
        #per lo stipendio metto un valore di default
        self.stipendio = stipendio
    ciao = 3;

    @classmethod
    def crea_oggetto_programmatore(cls):
        nome = input("Inserisci il nome del programmatore: ")
        cognome = input("Inserisci il cognome del programmatore: ")
        stipendio = input("Inserisci lo stipendio del programmatore: ")
        return cls(nome, cognome, stipendio)
    
class CJunior(CProgrammatore):
    def __init__(self, nome, cognome, stipendio, bonus = 500):
        super().__init__(nome, cognome, stipendio)
        #per il bonus metto un valore di default
        self.bonus = bonus
    
    def info(self):
        print("I programmatori Junior sono programmatori con meno di 5 anni di esperienza")

class CSenior(CProgrammatore):
    def __init__(self, nome, cognome, stipendio, bonus = 1000):
        super().__init__(nome, cognome, stipendio)
        #per il bonus metto un valore di default
        self.bonus = bonus
    
    def info(self):
        print("I programmatori Senior sono programmatori con piu' di 5 anni di esperienza")


