#!/opt/homebrew/bin/python3

class CCliente():

  def __init__(self, nome, cognome, CF, telefono):
    self.nome = nome
    self.cognome = cognome
    self.CF = CF
    self.telefono = telefono

  def stampa_dati_cliente(self):
    print("nome: {}, cognome:{}, CF:{}, numero_telefono:{}".format(
      self.nome,self.cognome,self.CF,self.telefono))


