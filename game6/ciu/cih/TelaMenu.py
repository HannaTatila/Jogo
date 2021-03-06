import os

import pygame
from pygame.mixer import music

_author__ = 'Hanna e Neimar'


class TelaMenu:
    def __init__(self):
        pygame.init()
        self.tamanhotelax = 700
        self.tamanhotelay = 500
        self.tela = pygame.display.set_mode((self.tamanhotelax, self.tamanhotelay))
        pygame.display.set_caption("Mar&moto")
        self.cinza = (80,80,80)

    def exibe_imagem(self, caminhoimagem, nomeimagem, posicao):
        imagem = pygame.image.load(os.path.join(caminhoimagem, nomeimagem))
        self.tela.blit(imagem, (posicao.eixox, posicao.eixoy))
        return imagem

    def exibe_texto_menu(self, texto, tam, cor, posicao):
        fonte = pygame.font.SysFont("Agency FB", tam, False, False)
        t = fonte.render(texto, True, cor)
        self.tela.blit(t, (posicao.eixox, (self.tamanhotelay / 2) + posicao.eixoy))

    def exibe_mensagem_cadastro(self, texto, posicao):
        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        t = fonte.render(texto, True, self.cinza)
        self.tela.blit(t, (posicao.eixox, (self.tamanhotelay / 2) + posicao.eixoy))

    @staticmethod
    def exibe_musica(diretoriomusica, nomemusica):
        music.load(os.path.join(diretoriomusica, nomemusica))
        music.play(-1)
