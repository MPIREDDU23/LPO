#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

nome_e_cognome = "Albert Einstein"
nome = nome_e_cognome[:6] # "Albert"
cognome = nome_e_cognome[7:] # "Einstein"
print(nome) # Stampa "Albert"
print(cognome) # Stampa "Einstein"

# non è possibile modificare una stringa
# nome_e_cognome[0] = "B" # non è possibile modificare una stringa
# risultato -> 
# Albert 
# Einstein
# Traceback (most recent call last):
# File "/Users/marcopireddu/Library/CloudStorage/OneDrive-UniversitàdiCagliari/Programmazione web e orientata agli oggetti/LPO/ESERCIZI/LPO_2/stringhe.py", line 8, in <module>
#   nome_e_cognome[0] = "B" # non è possibile modificare una stringa
#   ~~~~~~~~~~~~~~^^^
# TypeError: 'str' object does not support item assignment

