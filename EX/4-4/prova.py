# creare la classe CListaElementiUnici che eredita dalla classe built-in lista

class CListaElementiUnici(list):
    def append(self, object):
        # controlla se l'oggetto è già presente nella lista
        if object in self:
            print(f"Elemento {object} già presente nella lista.")
            return
        # se non è presente, lo aggiunge
        super().append(object)

lista = CListaElementiUnici()
# aggiunge un elemento alla lista
lista.append(1)
# aggiunge un elemento già presente alla lista
lista.append(1)
# aggiunge un altro elemento alla lista
lista.append(2)
# stampa la lista
print(lista)  # Output: [1, 2]C