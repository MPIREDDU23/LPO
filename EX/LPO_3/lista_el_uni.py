#!/opt/homebrew/bin/python3

class CListaElementiUnici(list):
    def append(self, elemento):
        if elemento not in self:
            super().append(elemento)
        else:
            print("L'elemento è già presente nella lista.")

# Esempio di utilizzo
lista = CListaElementiUnici()
lista.append(1)
lista.append(2)
lista.append(1)  # L'elemento è già presente nella lista. # Questo non verrà aggiunto
print(lista)  # Output: [1, 2]