# in python una classe può ereditare da più classi
# in questo caso si parla di eredità multipla

class A():
    def metodo_A(self):
        print("metodo di A")

class B():
    def metodo_B(self):
        print("metodo di B")

class C(A, B):
    pass

# in questo caso la classe C eredita da A e B
# i metodi
oggetto = C()
oggetto.metodo_A()
oggetto.metodo_B()


print("#############################")
print("nomi dei metodi uguali")
# se i metodi hanno lo stesso nome
class A():
    attr = 'A'
    def metodo(self):
        print("metodo di A")
class B():
    attr = 'B'
    def metodo(self):
        print("metodo di B")
    def metodo2(self):
        print("metodo2 di B")
class C(A, B):
    pass

# in questo caso la classe C eredita da A e B
# i metodi e li attributi, ma per i metodi(attributi)
#  con lo stesso nome viene scelto quello dellla 
# prima classe specificata

oggetto = C()
oggetto.metodo() # metodo di A
oggetto.metodo2() # metodo2 di B
print(oggetto.attr) # A

