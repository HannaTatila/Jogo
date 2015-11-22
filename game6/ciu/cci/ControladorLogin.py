from ciu.cci.ControladorCadastro import ControladorCadastro
from ciu.cih.TelaMenu import TelaMenu
from cln.cgt.AplCadastrarJogador import AplCadastrarJogador

_author__ = 'Hanna e Neimar'


class ControladorLogin(ControladorCadastro):

    def __init__(self):
        self.telamenu = TelaMenu()
        self.aplcadastrarjogador = AplCadastrarJogador()
        self.lopcoes = ["LOGIN:", "SENHA:"]
        self.nomecorrente = []
        self.nome = ""
        self.posicaoimprimenome = 270

    def enviar_dados_jogador(self, ldadosjogador):
        if self.aplcadastrarjogador.validar_login(ldadosjogador):
            return True
        else:
            return False