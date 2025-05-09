#!/usr/bin/env python3

# dizionari -> coppie chiave-valore

data = {
    'giorno': '10',
    'mese': '3',
    'anno': '2025'
}
# dizionario = {chiave: valore}
# per recuperare il valore associato alla chiave 'giorno'
print(data['giorno']) # Stampa '10'

# dizionario vuoto
data = {}

# aggiungere un elemento al dizionario
data['giorno'] = '10'
data['mese'] = '3'
data['anno'] = '2025'
print(data) # Stampa {'giorno': '10', 'mese': '3', 'anno': '2025'}