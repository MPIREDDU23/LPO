#!/opt/homebrew/bin/python3

class CStudente:
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

    @classmethod
    def crea_oggetto_studente(cls):
        nome = input("Inserisci il nome dello studente: ")
        cognome = input("Inserisci il cognome dello studente: ")
        matricola = input("Inserisci la matricola dello studente: ")
        return cls(nome, cognome, matricola)

def main():
    studente = CStudente.crea_oggetto_studente()
    print(f"Studente: {studente.nome} {studente.cognome},   {studente.matricola}")

class CStudenteSuperiori:
    def __init__(self, cognome, anno):
        self.cognome = cognome 
        self.anno = anno
    
    @property
    def cognome(self):
        return self.cognome
    
    @property
    def anno(self):
        return self.anno
    
    @anno.setter
    def anno(self, value):
        self.anno = value
    
    

if __name__ == "__main__":
    main()
