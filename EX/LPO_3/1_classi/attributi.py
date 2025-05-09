# attributi di istanza -> specifici per ogni oggetto
# attributi di classe -> condivisi tra tutti gli oggetti

class CDipendente:
    def __init__(self, nome, cognome):
        self.nome = nome # attributo di istanza
        self.cognome = cognome # attributo di istanza

class CAmministrativo(CDipendente):
    stipendio = 1500 # attributo di classe
    def __init__(self, nome, cognome):
        super().__init__(nome, cognome,)

class COperaio(CDipendente):
    stipendio = 1200 # attributo di classe
    def __init__(self, nome, cognome):
        super().__init__(nome, cognome,)

dipendente1 = CAmministrativo("Mario", "Rossi")
dipendente2 = COperaio("Luigi", "Verdi")
print(f"Lo stipendio di {dipendente1.nome} è {dipendente1.stipendio}" )
print(f"lo stipendio di un amministrativo è", CAmministrativo.stipendio)  
print(dipendente2.stipendio)

