from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class PeixePerseguidor(Obstaculo):
    def __init__(self, posicao):
        super(PeixePerseguidor, self).__init__("peixeperseguidor", posicao, 9, 4, TipoMovimento.reto)
