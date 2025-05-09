#!/usr/bin/env python3

class CEsame():
    def __init__(self, nome_esame, voto_esame):
        self._nome_esame = nome_esame
        self._voto_esame = voto_esame
    
    # per creare il setter, prima serve il getter
    # (questo è ovvio, per adesso esiste '_nome_esame'
    # se nessuno dichiara '_nome_esame', non si può chiamare)

    @property
    def voto_esame(self):
        return self._voto_esame

    @voto_esame.setter
    def voto_esame(self, voto):
        self._voto_esame = voto
    
    