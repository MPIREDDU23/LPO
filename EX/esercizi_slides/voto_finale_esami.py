#!/opt/homebrew/bin/python3

class CVoto_esame:
    def __init__(self, nome_esame: str, voto_primo_parzziale: int, voto_secondo_parziale: int):
        self.nome_esame = nome_esame
        self.voto_primo_parzziale = voto_primo_parzziale
        self.voto_secondo_parziale = voto_secondo_parziale

    #metodo privato per calcolare la media
    def _calcola_media(self):
        return (self.voto_primo_parzziale + self.voto_secondo_parziale) / 2
    
    @property
    def voto(self):
        return self._calcola_media()


class CRegistro_esami:
    def __init__(self):
        self.voti = []
    
    # funzione publica per aggiungere un voto
    def aggiungi_voto(self, voto: CVoto_esame):
        self.voti.append(voto)
    
    # funzione pubblica per stampare i voti
    def stampa_voti(self):
        for voto in self.voti:
            print(f"Esame: {voto.nome_esame}, Voto: {voto.voto}")

