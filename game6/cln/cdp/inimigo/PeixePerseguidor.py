import copy
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class PeixePerseguidor(Obstaculo):
    def __init__(self):
        super(PeixePerseguidor, self).__init__("peixeperseguidor", EstiloElementos.posicao_inimigo(), 9, 4, TipoMovimento.reto)

    @staticmethod
    def __copy__(self):
        return PeixePerseguidor()
