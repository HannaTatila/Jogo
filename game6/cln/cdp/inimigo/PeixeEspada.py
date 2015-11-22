import copy
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class PeixeEspada(Obstaculo):
    def __init__(self):
        super(PeixeEspada, self).__init__("peixeespada", EstiloElementos.posicao_inimigo(), 9, 7, TipoMovimento.subindo)

    @staticmethod
    def __copy__(self):
        return PeixeEspada()
