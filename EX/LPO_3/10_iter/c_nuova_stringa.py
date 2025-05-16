#!/opt/homebrew/bin/python3

from ogg_iteratori import CIteratore2Elementi
class CNuovaStringa():
    def __init__(self, stringa):
        self._stringa = stringa
    
    def __iter__(self):
        return CIteratore2Elementi(self._stringa)
    
s = "Ciao, come stai?"
ogg = CNuovaStringa(s)
for c in ogg:
    print(c)
