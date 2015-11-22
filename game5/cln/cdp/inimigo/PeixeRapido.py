from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class PeixeRapido(Obstaculo):
    def __init__(self, posicao):
        super(PeixeRapido, self).__init__("peixerapido", posicao, 33, 0, TipoMovimento.reto)
