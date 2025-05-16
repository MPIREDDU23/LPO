#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

# def <function_name>(<parameter_name>, ..., <parameter_name>):
#     """
#     <description>
#     """
#     <code>
#     return <value>

def primo_elemento(lista):
    """
    Restituisce il primo elemento della lista.
    """
    return lista[0] # Restituisce il primo elemento della lista


def minore_di(num_1, num_2):
    """
    Restituisce True se num_1 è minore di num_2, False altrimenti.
    """
    return num_1 < num_2 # Restituisce True se num_1 è minore di num_2, False altrimenti

minore_di(10, 20) # Restituisce True
minore_di(20, 10) # Restituisce False

# valori default
def somma(a=0, b=0):
    """
    Restituisce la somma di a e b.
    Se a e b non sono forniti, restituisce 0.
    """
    return a + b # Restituisce la somma di a e b

# si mettono alla fine
def somma(a, b=10):
    """
    Restituisce la somma di a e b.
    Se b non è fornito, restituisce a.
    """
    return a + b # Restituisce la somma di a e b
# se si mettono all'inizio, da errore

# molti parametri default
def somma(a=0, b=0, c=0):
    """
    Restituisce la somma di a, b e c.
    Se a, b e c non sono forniti, restituisce 0.
    """
    return a + b + c # Restituisce la somma di a, b e c
# voglio definire solo c

somma(c=3) # Restituisce 3

# si può fare anche
somma(c=3, a=1) # Restituisce 4
# il codice è però più difficile da leggere
# meglio utilizzare questa feature solo se 
# si vogliono "saltare" alcuni parametri

def primo_e_ultimo(lista):
    """
    Restituisce il primo e l'ultimo elemento della lista.
    """
    return lista[0], lista[-1] # Restituisce il primo e l'ultimo elemento della lista

primo, ultimo = primo_e_ultimo([1, 2, 3, 4, 5]) # Restituisce il primo e l'ultimo elemento della lista
print(primo) # Stampa 1
print(ultimo) # Stampa 5
# <valore>, <valore> = (<elemento>, <elemento>)

contatore = 0

def stampa():
    print(contatore) # Stampa il valore di contatore
    # contatore = contatore + 1 # non funziona, contatore non è definito


stampa() # Stampa 0




def mostra():
    print(contatore[0]) # Stampa il valore di contatore
    contatore[0] = contatore[0] + 1 # Funziona, contatore è una lista
    # la modifica della lista si riflette anche all'esterno

contatore = [1]

mostra() # Stampa 1
print(contatore) # Stampa 2

#passaggio per riferimento

def cambia_primo_elemento(lista, nuovo_valore):
    """
    Cambia il primo elemento della lista.
    """
    lista[0] = nuovo_valore # Cambia il primo elemento della lista
    # la modifica della lista si riflette anche all'esterno

lista = [1, 2, 3, 4, 5] # Lista
print("\nLISTA ORIGINALE")
print(lista) # Stampa [1, 2, 3, 4, 5] # La lista originale
cambia_primo_elemento(lista, 10) # Cambia il primo elemento della lista
print("\nLISTA MODIFICATA")
print(lista) # Stampa [10, 2, 3, 4, 5] # La modifica della lista si riflette anche all'esterno

