class CCliente():
    def __init__(self, nome_cliente, numero_telefono):
        self.nome = nome_cliente
        self.numero_telefono = numero_telefono


class CPersona(CCliente):
    def __init__(self, nome, cognome, eta):
        super().__init__(nome, None)

    def stampa_numero_di_telefono(self):
        print("il numero di telefono della persona è: ", self.numero_telefono)

class CAzienda(CCliente):
    def __init__(self, nome_azienda, numero_telefono):
        super().__init__(nome_azienda, numero_telefono)
    
    def stampa_numero_di_telefono(self):
        print("il numero di telefono dell'azienda è: ", self.numero_telefono)

# il codice si comporta in modo differente in base alla sottoclasse
# POLIMORFISMO


    

