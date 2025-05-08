from .c_cliente import CCliente

class CAzienda(CCliente):

    def __init__(self, partita_iva, idx, numero_telefono):
        self.partita_iva = partita_iva
        super(CAzienda, self).__init__(idx, numero_telefono)
