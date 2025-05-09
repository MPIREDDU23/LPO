#!/usr/bin/env python3

import re

# Esercizio 1
"""
Supponi che lindirizzo e-mail possa essere 
    anna-bi.anchi@tiscali.it
voglio estrarre 'tiscali'

Scrivi un'espressione regolare che estragga
il dominio dell'indirizzo e-mail

"""

email = "anna-bi.anchi@tiscali.it"

email_regex = r"[a-zA-Z]+[-][a-zA-Z0-9._%+-]{2}\.[a-zA-Z0-9._%+-]+@([a-zA-Z0-9._%+-]+)\.([a-zA-Z]{2,})"
# r indica che la stringa è raw, quindi non viene interpretata
# @ indica che vogliamo trovare la parte dopo il simbolo @
# [a-zA-Z0-9._%+-]+ indica che vogliamo trovare una o più lettere, numeri o caratteri speciali
# . indica che vogliamo trovare un punto
# [a-zA-Z]{2,} indica che vogliamo trovare due o più lettere dopo il punto
match = re.search(email_regex, email)
# re.search cerca una corrispondenza nell'intera stringa

if match:
    # se c'è una corrispondenza, estraiamo il dominio
    # group(1) restituisce il primo gruppo di cattura, che è il dominio
    # match.group(0) restituisce l'intera corrispondenza
    domain = match.group(1)
    print(f"Il dominio dell'indirizzo e-mail è: {domain}")
else:
    print("Nessun dominio trovato nell'indirizzo e-mail.")

