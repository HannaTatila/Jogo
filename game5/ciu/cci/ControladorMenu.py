from _operator import concat
import pygame
from pygame import KEYDOWN
from pygame import QUIT, K_DOWN, K_UP, K_RETURN, K_ESCAPE
from ciu.cci import ControladorLogin
from ciu.cci.ControladorCadastro import ControladorCadastro

from ciu.cci.ControladorJogo import ControladorJogo
from ciu.cci.ControladorLogin import ControladorLogin
from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from principal.CaminhoRecursos import CaminhoRecursos

__author__ = 'dell'


class ControladorMenu():
    CONST_POSICAOX_SETA = 245
    CONST_POSICAOY_SETA = 260
    CONST_POSICAOX_OPCAO_MENU = 302
    CONST_POSICAOY_OPCAO_MENU = 30
    CONST_DISTANCIA_OPCAO_MENU = 40
    CONST_TAMANHO_OPCAO_MENU_PADRAO = 30
    CONST_TAMANHO_OPCAO_MENU_SELECAO = 40

    def __init__(self,controladorjogo):
        pygame.init()
        self.telamenu = TelaMenu()
        self.caminhoimagem = CaminhoRecursos.caminho_imagens()
        self.controladorjogo = controladorjogo
        self.controladorcadastro = ControladorCadastro()
        self.controladorlogin = ControladorLogin()
        self.lopcoes = ["INICIAR","CADASTRAR","CONFIGURACOES","SAIR"]
        self.mensagemsucesso = "Jogador cadastrado com sucesso!"
        self.mensagemerro = "Login informado ja existe!"
        self.mensagemdadoinvalido = "Os dados informados nao sao validos!"
        self.preto = (0,0,0)
        self.cinza = (80,80,80)

    def exibir_tela_menu(self):
        self.telamenu.exibe_imagem(self.caminhoimagem, "fundo2.jpg", EstiloElementos.posicao_imagem_fundo())
        self.telamenu.exibe_imagem(self.caminhoimagem, "nome2.png", EstiloElementos.posicao_titulo_jogo())

    def exibir_musica(self):
        self.telamenu.exibe_audio(CaminhoRecursos.caminho_musicas(), "music1.mp3")

    def exibe_opcoes_menu(self, menuselecao):
        alteraposicao = 0
        for id, opcao in enumerate(self.lopcoes):
            tam = self.CONST_TAMANHO_OPCAO_MENU_PADRAO
            cor = self.cinza
            if id+1 == menuselecao:
                tam = self.CONST_TAMANHO_OPCAO_MENU_SELECAO
                cor = self.preto
            self.telamenu.exibe_texto_menu(opcao, tam, cor, Posicao(self.CONST_POSICAOX_OPCAO_MENU, self.CONST_POSICAOY_OPCAO_MENU + alteraposicao))
            alteraposicao = alteraposicao + self.CONST_DISTANCIA_OPCAO_MENU


    def exibe_tela_mensagem_cadastro(self, mensagem):
        self.manipula_seta(2)
        self.telamenu.exibe_mensagem_cadastro(mensagem, EstiloElementos.posicao_mensagem_cadastro())
        self.telamenu.exibe_texto_menu("VOLTAR", self.CONST_TAMANHO_OPCAO_MENU_SELECAO, self.preto, Posicao(self.CONST_POSICAOX_OPCAO_MENU, 70))
        pygame.display.flip()


    def manipula_seta(self, menuselecao):
        if (menuselecao >= 1) & (menuselecao <= len(self.lopcoes)):
            self.telamenu.exibe_imagem(self.caminhoimagem, "seta.gif", Posicao(self.CONST_POSICAOX_SETA, self.CONST_POSICAOY_SETA + 40*(menuselecao-1) ))

    def menu_selecao(self, menuselecao):
        ## TELA MENU PRINCIPAL
        if (menuselecao >= 1) & (menuselecao <= len(self.lopcoes)):
            self.exibe_opcoes_menu(menuselecao)

        ## REGRAS DA TELA MENU PRINCIPAL:
        elif (menuselecao < 1) | (menuselecao == 113) | (menuselecao == 213) | (menuselecao == 216):
            menuselecao = 1    # nao incrementar estado se apertar p cima de novo
        elif menuselecao == len(self.lopcoes)+1 :
            menuselecao = len(self.lopcoes)    # nao incrementar estado se apertar p baixo de novo

        elif (menuselecao == 11) | (menuselecao == 99) | (menuselecao == 101):
            menuselecao = 100    # se der enter na opcao 'INICIAR'
        elif (menuselecao == 12) | (menuselecao == 199) | (menuselecao == 201):
            menuselecao = 200    # se der enter na opcao 'CADASTRAR'
        elif menuselecao == 13:
            menuselecao = 3   # PARA, POR ENQUANTO, NAO FUNCIONAR NADA EM CONFIGURACOES
        elif menuselecao == 14:
            exit()    # se der enter na opcao 'SAIR'

        ## TELA LOGIN
        elif menuselecao == 100:
            self.controladorlogin.exibe_tela_informar_dados()
            if self.controladorlogin.cadastro():
                self.controladorjogo.jogo()
            else:
                menuselecao = 103
                self.exibe_tela_mensagem_cadastro(self.mensagemdadoinvalido)

        ## REGRAS DA TELA LOGIN
        elif menuselecao == 103:
            self.exibe_tela_mensagem_cadastro(self.mensagemdadoinvalido)
        #elif (menuselecao == 113) | (menuselecao == 213) | (menuselecao == 216):
         #   menuselecao = 1
        #elif (menuselecao == 99) | (menuselecao == 101):
         #   menuselecao = 100
        elif (menuselecao == 102) | (menuselecao == 104):
            menuselecao = 103

        ## TELA CADASTRO
        elif menuselecao == 200:
            self.controladorcadastro.exibe_tela_informar_dados()
            if self.controladorcadastro.cadastro():
                menuselecao = 203
                self.exibe_tela_mensagem_cadastro(self.mensagemsucesso)
            else:
                menuselecao = 206
                self.exibe_tela_mensagem_cadastro(self.mensagemerro)
        elif menuselecao == 203:
            self.exibe_tela_mensagem_cadastro(self.mensagemsucesso)
        elif menuselecao == 206:
            self.exibe_tela_mensagem_cadastro(self.mensagemerro)

        ## REGRAS DA TELA CADASTRO
        #elif (menuselecao == 199) | (menuselecao == 201):
            #menuselecao = 200
        elif (menuselecao == 202) | (menuselecao == 204):
            menuselecao = 203
        elif (menuselecao == 205) | (menuselecao == 207):
            menuselecao = 206
       # elif (menuselecao == 213) | (menuselecao == 216):
        #    menuselecao = 1

        return menuselecao


    def menu(self):
        menuselecao = 1
        #self.exibir_musica()
        while True:
            self.exibir_tela_menu()
            self.manipula_seta(menuselecao)
            menuselecao = self.menu_selecao(menuselecao)
            pygame.display.update()
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()
                if e.type == KEYDOWN:
                    if e.key == K_DOWN:
                        menuselecao += 1
                    elif e.key == K_UP:
                        menuselecao -= 1
                    elif e.key == K_RETURN:
                        menuselecao += 10
                    elif e.key == K_ESCAPE:
                        menuselecao -= 10