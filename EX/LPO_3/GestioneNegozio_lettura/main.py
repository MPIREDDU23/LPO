#!/opt/homebrew/bin/python3

from gestione_clienti.c_clienti import CClienti
from dati.path import PATH_DATA_DIR

clienti = CClienti(PATH_DATA_DIR)

clienti.stampa_dati_clienti()









