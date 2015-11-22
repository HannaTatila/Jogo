import pygame
from pygame.constants import KEYDOWN, K_RETURN, K_SPACE
from ciu.cih.TelaMenu import TelaMenu
from cln.cgt.AplCadastrarJogador import AplCadastrarJogador
from cln.cdp.Posicao import Posicao

__author__ = 'dell'


class ControladorCadastro:

    def __init__(self):
        self.telamenu = TelaMenu()
        self.aplcadastrarjogador = AplCadastrarJogador()
        self.lopcoes = ["LOGIN:", "SENHA:"]
        self.nomecorrente = []
        self.nome = ""
        self.posicaoimprimenome = 270

    def exibe_tela_informar_dados(self):
        alteraposicao = 0
        for id, opcao in enumerate(self.lopcoes):
            self.telamenu.exibe_texto_menu(opcao, 40, (0,0,0), Posicao(105, 25 + alteraposicao))
            pygame.draw.rect(self.telamenu.tela, (255, 255, 255), (220, 270 + alteraposicao, 300, 30), 0)
            alteraposicao = alteraposicao + 40

        self.telamenu.exibe_texto_menu("CONFIRMAR", 40, (0,0,0),Posicao(302, 120))
        pygame.display.flip()

    @staticmethod
    def get_key():
        while 1:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key

    def imprime_nome(self):
        tela = self.telamenu.tela
        self.nome = ""
        for i in range(len(self.nomecorrente)):
            self.nome = self.nome + self.nomecorrente[i]

        fonte = pygame.font.SysFont("ARIAL", 24, False, False)
        texto = fonte.render(self.nome, True, (0, 0, 0))
        tela.blit(texto, (225, self.posicaoimprimenome))
        pygame.display.flip()


    def enviar_dados_jogador(self, ldadosjogador):
        if self.aplcadastrarjogador.cadastrar_jogador(ldadosjogador):
            return True
        else:
            return False

    def cadastro(self):
        ldadosjogador = []
        while True:
            tecla = self.get_key()
            if tecla == K_RETURN:
                ldadosjogador.append(self.nome)
                self.nome = ""
                self.nomecorrente = []
                if len(ldadosjogador) == len(self.lopcoes):
                    self.posicaoimprimenome = 270
                    if self.enviar_dados_jogador(ldadosjogador):
                        return True
                    else:
                        return False
                else:
                    self.posicaoimprimenome = self.posicaoimprimenome + 40
            elif tecla <= 127:
                self.nomecorrente.append(chr(tecla))
                self.imprime_nome()