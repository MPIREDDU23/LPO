#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

class CCliente:
    def __init__(self, idx: int, __numero_telefono: str):
        self.__idx = idx
        self.__numero_telefono = __numero_telefono

    def get_idx(self) -> int:
        return self.__idx
    def set_idx(self, idx: int) -> None:
        self.__idx = idx

    def get_numero_telefono(self) -> str:
        return self.__numero_telefono
    def set_numero_telefono(self, numero_telefono: str) -> None:
        self.__numero_telefono = numero_telefono
    
class CPersona(CCliente):
    def __init__(self, idx: int, nome: str, cognome: str, numero_telefono: str):
        super().__init__(idx, numero_telefono)
        self.nome = nome
        self.cognome = cognome

class CAzienda(CCliente):
    def __init__(self, idx: int, nome_azienda: str, numero_telefono: str):
        super().__init__(idx, numero_telefono)
        self.nome_azienda = nome_azienda

class CLista_clienti:
    def __init__(self):
        self.__lista_clienti = []
    
    def aggiungi_cliente(self, cliente: CCliente) -> None:
        self.__lista_clienti.append(cliente)
    
    def stampa_clienti(self) -> None:
        for cliente in self.__lista_clienti:
            if isinstance(cliente, CPersona):
                print(f"ID: {cliente.get_idx()}, Nome: {cliente.nome}, Cognome: {cliente.cognome}, Telefono: {cliente.get_numero_telefono()}")
            elif isinstance(cliente, CAzienda):
                print(f"ID: {cliente.get_idx()}, Nome Azienda: {cliente.nome_azienda}, Telefono: {cliente.get_numero_telefono()}")


# Esempio di utilizzo

lista_clienti = CLista_clienti()

cliente1 = CPersona(1, "Mario", "Rossi", "123456789")
cliente2 = CAzienda(2, "ACME Corp.", "987654321")


lista_clienti.aggiungi_cliente(cliente1)
lista_clienti.aggiungi_cliente(cliente2)
lista_clienti.__lista_clienti = [cliente1, cliente2]  # Accesso diretto alla lista per la stampa

# Stampa dei clienti
print("Lista Clienti:")
lista_clienti.stampa_clienti()

lista_clienti.stampa_clienti()