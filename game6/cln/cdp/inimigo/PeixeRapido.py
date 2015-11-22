import copy
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class PeixeRapido(Obstaculo):
    def __init__(self):
        super(PeixeRapido, self).__init__("peixerapido", EstiloElementos.posicao_inimigo(), 33, 0, TipoMovimento.reto)

    @staticmethod
    def __copy__(self):
        return PeixeRapido()