#!/usr/bin/env python3

from .c_cliente import CCliente

class CPersona(CCliente):

    def __init__(self, nome, cognome, anno_nascita, idx, numero_telefono):

        self.nome = nome
        self.cognome = cognome
        self.anno_nascita = anno_nascita
        super(CPersona, self).__init__(idx, numero_telefono)