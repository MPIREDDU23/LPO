#!/opt/homebrew/bin/python3

class CStringa:
    def __init__(self, string):
        self._lunghezza = None # definiamo l'attributo di sola lettura
        self._string = self._controlla_string(string)
    
    def _calcola_lunghezza(self):
        return len(self._string)
    @property
    def lunghezza(self):
        return self._lunghezza
    
    @property
    def string(self):
        return self._string
    @string.setter
    def string(self, string):
        self._string = self._controlla_string(string)
        self._lunghezza = self._calcola_lunghezza()