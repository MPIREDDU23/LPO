# se il progetto è di grande dimensioni, è meglio usare i packages
# che organizzano il codice in moduli
# un pacchetto è una cartella che organizza diversi moduli

"""
progetto_ecommerce (dir)
    main.py
    ecommerce (dir)
        __init__.py
        database.py
        prodotti.py
"""
# se il nostro progetto è organizzaro in quwsto modo
# per importare un modulo ad esempio nel main.py
# from <percorso> importa <nome_funzione_o classe>
# separiamo ogni cartella con un punto

# from ecommerce.database import Database
# questo è un import assoluto


# si possono specificare anche import relativi
# per riferirsi a moduli che si trovano nello stesso package
# from .<nome_file> import <nome_funzione_o_classe>

# se vofliamo accedere alla classe CProdotto definita in 
# prodotti.py, dallo script database.py, che si trova nello 
# stesso package
# from .prodotti import CProdotto

# se vofliamo riferirci a un modulo che si trova in un package padre
# from ..<nome_file> import <nome_funzione_o_classe>

"""
progetto_ecommerce (dir)
    main.py
    ecommerce (dir)
        __init__.py
        database.py
        prodotti.py
        payment (dir)
            __init__.py
            payment.py
"""
# ad esempio da payment.py vogliamo importare la classe CProdotto
# from ..prodotti import CProdotto

# diversi modi per effettuare l'import in modo che il progetto
# funzioni correttamente
# 1. import relativo, quando il modulo si trova dentro il package
#   e si vuole che quel modulo possa essere importato da altri moduli
#   ma non eseguito direttamente
# 2. import assoluto, quando il modulo deve essere eseguito
#   direttamente e non deve essere importato da altri moduli



