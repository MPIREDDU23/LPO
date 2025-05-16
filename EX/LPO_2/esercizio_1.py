#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

# Scrivete un programma che acquisisca in input una sequenza
# di numeri e li memorizzi in una tupla. (I numeri dovranno
# essere acquisiti uno alla volta).

tupla = () # una tupla vuota

quanti_numeri = int(input("Quanti numeri vuoi inserire? "))

cont = 0
while cont < quanti_numeri:
    n = float(input("Inserisci un numero: "))
    tupla += (n,) # aggiungi il numero alla tupla
    cont += 1

print(tupla) # Stampa la tupla

