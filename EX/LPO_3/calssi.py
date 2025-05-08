# sintassi della dichiarazione di una classe class C<ClassName>
# una classe è un tipo di dato definito dall'utente

class CStudente:
    # costruttore
    # metodo speciale che viene chiamato quando si crea un oggetto
    # self è un riferimento all'istanza della classe
    # serve a mostrare gli attributi 

    def __init__(self, nome, cognome, matricola):
        # attributi della classe
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        # attributi privati # attenzione, gli attributi rimangono sempre e comunque accessibili dall'esterno
            # self.__anno_nascita = 2000
        # attributi protetti
            # self._anno_nascita = 2000
        # attributi pubblici
        self.anno_nascita = 2000

        # la differenza tra attributi privati e protetti è che
        # gli attributi privati non possono essere accessibili
        # al di fuori della classe
        # gli attributi protetti possono essere accessibili
        # al di fuori della classe ma non dovrebbero essere
        # utilizzati direttamente

    # attributi della classe
    # sono condivisi tra tutte le istanze della classe
    # sono dichiarati all'interno della classe
    # ma al di fuori di qualsiasi metodo
    anno_accademico = (2024, 2025)

    # metodi della classe

    def stampa_studente(self):
        print(f"Nome: {self.nome}")
        print(f"Cognome: {self.cognome}")
        print(f"Matricola: {self.matricola}")
        print(f"Anno di nascita: {self.anno_nascita}")
        print(f"Anno accademico: {self.anno_accademico}")

# relazione di aggregazione
# una classe contiene un'altra classe
# se l'istanza viene distrutta
# l'istanza della classe contenuta non viene distrutta
class CCorso:
    def __init__(self, nome, codice):
        self.nome = nome
        self.codice = codice
        self.studenti = []

    def aggiungi_studente(self, studente):
        self.studenti.append(studente)
    

class CLibro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

#relazione di composizione
# una classe contiene un'altra classe, se l'istanza viene distrutta
# anche l'istanza della classe contenuta viene distrutta

class CBiblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.libri = []
    
    def aggiungi_libro(self):
        nome = input("Inserisci il nome del libro: ")
        autore = input("Inserisci il nome dell'autore: ")
        libro = CLibro(nome, autore)
        self.libri.append(libro)
    # il riferimento ai libri esiste solo all'interno della biblioteca
    # se la biblioteca viene distrutta
    # anche i libri vengono distrutti


# relazione di ereditarietà
# una classe deriva da un'altra classe
# i borsisti sono studenti

class CBorsista(CStudente):
    def __init__(self, nome, cognome, matricola, stipendio):
        # chiamata al costruttore della classe padre
        super().__init__(nome, cognome, matricola)
        self.stipendio = stipendio
        # gli attributi e i metodi della classe padre 
        # sono accessibili
        # all'interno della classe figlia
    
    # riscrivo la funzione della classe padre
    # per aggiungere il nuovo attributo stipendio
    # posso anche usare il metodo della classe padre
    # per non riscrivere il codice
    def stampa_studente(self):
        # chiamata al metodo della classe padre
        super().stampa_studente()
        print(f"Stipendio: {self.stipendio}")
        # gli attributi e i metodi della classe padre 
        # sono accessibili
        # all'interno della classe figlia
    # stampa_studente è un override del metodo della classe padre
    # quando viene chiamato il metodo, viene eseguito il codice più vicino. 

    
borsista = CBorsista("Mario", "Rossi", 123456, 1000)

borsista.stampa_studente() # uso il metodo della classe CStudente





