#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

from collections.abc import Iterator

class CIteratore2Elementi(Iterator):
    def __init__(self, lista: str, hop = 2):
        self._lista = lista
        self._hop = hop
        self._idx = 0

    def __next__(self):
        if len(self._lista) > self._idx + self._hop:
            l = self._lista[self._idx:self._idx+self._hop]
            self._idx = self._idx + self._hop
            return l
        else: 
            raise StopIteration
            l = self._lista[self._idx:]
            phop = self._hop
            self._hop = self._hop - len(self._lista) + self._idx
            self._idx = 0
            
            l = l + self.__next__()

            self._hop = phop
            return l

class CNuovaStringa:
    def __init__(self, stringa: str):
        self._stringa = stringa
    
    def __iter__(self):
        return CIteratore2Elementi(self._stringa)

s = CNuovaStringa("cwkjcmweklvmewkl")
for el in s:
    print(el)


        