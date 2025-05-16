#!/opt/homebrew/bin/python3

lista = [] # lista vuota

quanti_numeri = int(input("Quanti numeri vuoi inserire? "))

for i in range(quanti_numeri):
    numero = float(input(f"Inserisci il numero {i+1}: "))
    lista += [numero] # aggiunge il numero alla lista
    # lista.append(numero) # aggiunge il numero alla lista
    # lista.insert(i, numero) # aggiunge il numero alla lista
    # # lista[i] = numero # aggiunge il numero alla lista, funziona solo se l'indice i esiste già 
    # lista.extend([numero]) # aggiunge il numero alla lista

print(f"La lista è ", lista)

def ordine_crescente(lista):
    for i in range(1, len(lista)):
        if lista[i] < lista[i-1]:
            return False
    return True

if ordine_crescente(lista):
    print("La lista è in ordine crescente")
else:
    print("La lista non è in ordine crescente")