from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class PeixeEspada(Obstaculo):
    def __init__(self, posicao):
        super(PeixeEspada, self).__init__("peixeespada", posicao, 9, 7, TipoMovimento.subindo)