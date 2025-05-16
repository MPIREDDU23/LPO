#!/opt/homebrew/bin/python3

from .c_cliente import CCliente
from copy import deepcopy

class CClienti():

  def __init__(self, path_dati_clienti):
    self._clienti = []

    self._path_file_clienti = deepcopy(path_dati_clienti)
    self._path_file_clienti = self._path_file_clienti.joinpath("dati_clienti.txt")

  # se usaste il percorso relativo sarebbe
  # self._path_file_clienti = "dati/dati_clienti.txt"

    print(self._path_file_clienti)

    self._carica_clienti_da_file()

  def _carica_clienti_da_file(self):
    with open(self._path_file_clienti, "r") as f_clienti:
      for riga in f_clienti.readlines():
        #rimuoviamo il carattere a capo
        riga_divisa = riga.split("\n")[0]

        #dividiamo in base al carattere separatore
        riga_divisa = riga_divisa.split(";")
        nome = riga_divisa[0]
        cognome = riga_divisa[1]
        CF = riga_divisa[2]
        n_telefono = riga_divisa[3]

        cliente = CCliente(nome, cognome, CF, n_telefono)
        self._clienti.append(cliente)

  def stampa_dati_clienti(self):
    for cliente in self._clienti:
      cliente.stampa_dati_cliente()