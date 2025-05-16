#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

# i metodi di istanza, sono i metodi che possono essere chiamati
# da un'istanza

# i metodi di classe, sono associati alla classe stessa


class CDipendente:
    stipendio = 1500
    
    def __init__(self, nome, cognome, anno):
        self.nome = nome
        self.cognome = cognome
        self.anno = anno
    
    # metodo di istanza
    def ottieni_nome(self):
        return self.nome
    
    # metodo di classe
    @classmethod
    def ottieni_stipendio(cls):
        return cls.stipendio

persona1 = CDipendente("Marco", "Pireddu", "2003")

print(persona1.ottieni_stipendio()) # uso il metodo di classe, per l'istanza
print(CDipendente.ottieni_stipendio()) # il risltato è lo stesso

print(persona1.ottieni_nome()) # uso il medodo di istanza, per l'istanza
# print(CDipendente.ottieni_nome()) # non funziona, non saprebbe a quale istanza riferirsi




class CStudente: 
    def __init__(self, nome, cognome, matricula):
        self.nome = nome
        self.cognome = cognome
        self.matricula = matricula
    

    '''
        costruttore alternativo
        per creare un oggetto di tipo CStudente
    '''
    @classmethod
    def crea_studente(cls):
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        matricula = input("Matricola: ")
        return cls(nome, cognome, matricula)
    

# metodi statici
# non hanno accesso a self o cls
# sono metodi che non dipendono da nessun oggetto

class CAnalista(CDipendente):
    stipendio_base = 2000

    def __init__(self, nome, cognome, anno, stipendio):
        super().__init__(nome, cognome, anno)
        self.stipendio_base = stipendio

    '''
        i metodi statici non hanno accesso a self o cls
        sono metodi che non dipendono da nessun oggetto
        possono essere chiamati senza creare un'istanza
    '''
    @staticmethod
    def info():
        print("Questa è una classe di analisti")


    