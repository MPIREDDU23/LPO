#!/opt/homebrew/bin/python3

# supponiamo di avere 4 classi
# class A()
# class B(A)
# class C(A)
# class D(B, C)

# come si implementano le __init__?

class A():
    def __init__(self):
        print("inizializzazione di A")

class B(A):
    def __init__(self):
        print("inizializzazione di B")
        A.__init__(self)
class C(A):
    def __init__(self):
        print("inizializzazione di C")
        A.__init__(self)

class D(B, C):
    def __init__(self):
        print("inizializzazione di D")
        B.__init__(self)
        C.__init__(self)

oggetto = D()
# stampa:
# inizializzazione di D
# inizializzazione di B
# inizializzazione di A
# inizializzazione di C
# inizializzazione di A

# dunque, due volte A
# in questo caso si parla di diamond problem
# per risolvere si può usare super().__init__()
# che non va a richiamare direttamente il costruttore della classe
# ma quello della classe padre, in modo che venga
# chiamato solo una volta

print("#############################")
print("super()")
class A():
    def __init__(self, clss:str):
        print("inizializzazione di A")
        print(clss)
class B(A):
    def __init__(self, clss:str):
        print("inizializzazione di B")
        print(clss)
        super().__init__("B")
class C(A):
    def __init__(self, clss:str):
        print("inizializzazione di C")
        print(clss)
        super().__init__("C")
class D(B, C):
    def __init__(self):
        print("inizializzazione di D")
        super().__init__("D")

oggetto = D()
# stampa:
# inizializzazione di D
# inizializzazione di B
# D
# inizializzazione di C
# B
# inizializzazione di A
# C 

# Apparentemente sembra che super().__init__(), eseguito da B
# chiami __init__() di C, ma se prendiamo un'istanza di B
# e chiamiamo super().__init__() in B, questo chiama
# __init__() di A, non di C.
# Questo è dovuto al fatto che super() restituisce
# la classe successiva nella MRO (Method Resolution Order)
# che è una lista di classi in cui Python cerca i metodi
# e gli attributi.

# rende difficile e poco chiaro l'ordine di chiamata. Dovremmo dunque 
# dare input differenti in base alla classe da cui chiamiamo

# l'ereditarià multipla è generalmente sconsigliata

