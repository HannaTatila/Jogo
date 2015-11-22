from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class Baiacu(Obstaculo):
    def __init__(self, posicao):
        super(Baiacu, self).__init__("baiacu", posicao, 9, 0, TipoMovimento.reto)
