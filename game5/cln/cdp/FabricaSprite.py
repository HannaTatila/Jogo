from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Personagem import Personagem
from cln.cdp.inimigo.Baiacu import Baiacu
from cln.cdp.inimigo.PeixeEspada import PeixeEspada
from cln.cdp.inimigo.PeixePerseguidor import PeixePerseguidor
from cln.cdp.inimigo.PeixeRapido import PeixeRapido

_author__ = 'Hanna e Neimar'


class FabricaSprite(object):

    @staticmethod
    def criar_sprite(tipo):
        posicao = EstiloElementos.posicao_inimigo()
        sprite = None
        if tipo == "peixeespada":
            sprite = PeixeEspada(posicao)
        elif tipo == "baiacu":
            sprite = Baiacu(posicao)
        elif tipo == "peixerapido":
            sprite = PeixeRapido(posicao)
        elif tipo == "peixeperseguidor":
            sprite = PeixePerseguidor(posicao)
        elif tipo == "personagem":
            sprite = Personagem(EstiloElementos.posicao_personagem())
        return sprite