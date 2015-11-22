from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class Baiacu(Obstaculo):
    def __init__(self):
        super(Baiacu, self).__init__("baiacu", EstiloElementos.posicao_inimigo(), 9, 0, TipoMovimento.reto)

    @staticmethod
    def __copy__(self):
        return Baiacu()
