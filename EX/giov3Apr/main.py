#!/opt/homebrew/bin/python3

#creare una mixin CAnalisiDuplicatiMixin

class CAnalisiDuplicatiMixin:
    def __init__(self, lista):
        self.lista = lista

    # conta_duplicati()
    #  
    # conta e restituisce gli elementi duplicati in una lista
    def conta_duplicati(self):
        contatore = {}
        for elemento in self.lista:
            if elemento in contatore:
                contatore[elemento] += 1
            else:
                contatore[elemento] = 1
        return contatore
    
    # cerca_duplicati()
    #
    # cerca e restituisce una lista degli elementi duplicati in una lista
    #
    def cerca_duplicati(self):
        contatore = {}
        duplicati = []
        for elemento in self.lista:
            if elemento in contatore:
                contatore[elemento] += 1
                if contatore[elemento] == 2:
                    duplicati.append(elemento)
            else:
                contatore[elemento] = 1
        return duplicati

    



class CStringa(CAnalisiDuplicatiMixin):
    def __init__(self, stringa):
        self.stringa = stringa
        super().__init__(stringa)

class CLista(CAnalisiDuplicatiMixin):
    def __init__(self, lista):
        self.lista = lista
        super().__init__(lista)

#provacle
s = CStringa("aaaabbbc")
l = CLista([1, 2, 3, 1, 2, 3])
print(l.conta_duplicati())
# Output: {1: 2, 2: 2, 3: 2}

print(s.conta_duplicati())
# Output: {a: 4, b: 3, c: 2}

print(l.cerca_duplicati())
# Output: [1, 2, 3]
print(s.cerca_duplicati())
# Output: [a, b, c]
