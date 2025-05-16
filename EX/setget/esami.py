#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

class CEsame:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def voto(self):
        return self.__voto
    @voto.setter
    def voto(self, voto):
        if voto < 0 or voto > 30:
            insert = input("Il voto inserito non è valido. Inserire un voto compreso tra 0 e 30: ")
            self.voto = int(insert)
        else:
            self.__voto = voto

#attributo stringa e attributo di sola lettura lunghezza stringa
class CStringa: 
    def __init__(self, stringa):
        self.stringa = stringa

    @property
    def stringa(self):
        return self.__stringa
    @stringa.setter
    def stringa(self, stringa):
        self.__stringa = stringa

    @property
    def lunghezza(self):
        return len(self.__stringa)

str = CStringa("Ciao")
print(str.lunghezza)