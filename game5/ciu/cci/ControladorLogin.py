from ciu.cci.ControladorCadastro import ControladorCadastro

__author__ = 'dell'

import pygame
from pygame.constants import KEYDOWN, K_RETURN, K_SPACE
from ciu.cih.TelaMenu import TelaMenu
from cln.cgt.AplCadastrarJogador import AplCadastrarJogador
from cln.cdp.Posicao import Posicao

__author__ = 'dell'


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