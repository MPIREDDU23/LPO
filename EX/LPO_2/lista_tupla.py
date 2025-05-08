tupla = (1,) # una tupla con un solo elemento
lista = [1] # una lista con un solo elemento
print(tupla) # Output: (1,)
print(lista) # Output: [1]

tupla = (1) # non è una tupla, è un intero
print(tupla) # Output: 1


voti = (30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0) # tupla
# oppure 
# voti = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0] # lista

print(voti[3]) # Stampa il voto alla posizione 3
print(voti[0:5]) # Stampa i primi 5 voti
print(voti[5:]) # Stampa i voti dalla posizione 5 in poi

print(voti[-1]) # Stampa l'ultimo voto
print(voti[-2]) # Stampa il penultimo voto
print(voti[-5:]) # Stampa gli ultimi 5 voti
print(voti[-5:-2]) # Stampa i voti dalla posizione -5 a -2

print(voti[1:-1]) # Stampa i voti dal secondo al penultimo

# per dichiarare una tupla si usano le parentesi tonde, se 
# l'elemento è una sola tupla si usa la virgola

voti = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0] # lista
primi_due_voti = voti[0:2] # copia i primi due voti in 'primi_due_voti'
primi_due_voti[0] = 18 # modifica il primo voto in 'primi_due_voti'
print(primi_due_voti) # Stampa i primi due voti, il primo voto è stato modificato
print(voti) # Stampa i voti originali, il primo voto non è stato modificato


# se invece passiamo la lista, le modifiche si riflettono anche nella
# lista originale

tutti_i_voti = voti # passa il riferimento alla lista
tutti_i_voti[0] = 18 # modifica il primo voto in 'tutti_i_voti'

print(tutti_i_voti) # Stampa i voti, il primo voto è stato modificato
print(voti) # Stampa i voti originali, il primo voto è stato modificato
tutti_i_voti[0] = 30 # modifica il primo voto in 'tutti_i_voti' e 'voti'

# per copiare senza passare il riferimento, usiamo voti[:]
tutti_i_voti = voti[:] # copia la lista
tutti_i_voti[0] = 18 # modifica il primo voto in 'tutti_i_voti'
print(tutti_i_voti) # Stampa i voti, il primo voto è stato modificato
print(voti) # Stampa i voti originali, il primo voto non è stato modificato



