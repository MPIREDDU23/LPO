from abc import ABC, abstractmethod
class CDipendente(ABC):

    @classmethod
    @abstractmethod
    def calcolaStipendio(cls, mese):
        pass
# definisco la classe astratta

class CProgrammatore(CDipendente):
    stipendio = 1500

    @classmethod
    def calcolaStipendio(cls, mese):
        if mese == 12:
            return cls.stipendio + 500
        return cls.stipendio
    
class CRagioniere(CDipendente):
    stipendio = 1300

    @classmethod
    def calcolaStipendio(cls, mese):
        if mese == 3:
            return cls.stipendio * 1.3
        return cls.stipendio

print(f"Stipendio programmatore[Dicembre]: {CProgrammatore.calcolaStipendio(12)}")
print(f"Stipendio programmatore[Marzo]: {CProgrammatore.calcolaStipendio(3)}")
print(f"Stipendio ragioniere[Dicembre]: {CRagioniere.calcolaStipendio(12)}")
print(f"Stipendio ragioniere[Marzo]: {CRagioniere.calcolaStipendio(3)}")
