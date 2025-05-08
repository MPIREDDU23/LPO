# for <variabile> in <iterabile>:
#     <istruzioni>

voti = (30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0) # tupla

for voto in voti:
    print(voto) # Stampa il voto

nome = "Albert Einstein"
for lettera in nome:
    print(lettera) # Stampa la lettera

diz = {
    'giorno': '10',
    'mese': '3',
    'anno': '2025'
}
for chiave in diz:
    print(chiave) # Stampa la chiave
    print(diz[chiave]) # Stampa il valore associato alla chiave

for n in range(3):
    print(n) # Stampa il numero


studente = {
    'nome': 'Marco',
    'cognome': 'Pireddu',
    'matricola': 123456,
    'anno-nascita': 2000,
}

for chiave in studente:
    print(chiave + ": " + str(studente[chiave])) # Stampa la chiave e il valore associato alla chiave

