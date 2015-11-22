import unittest

from cln.cgt.AplJogo import AplJogo

_author__ = 'Hanna e Neimar'


class Test(unittest.TestCase):
    
    def teste_aumenta_velocidade_personagem(self):
        apljogo = AplJogo()
        apljogo.aumenta_deslocamento()
        self.assertEqual(10, apljogo.personagem.velocidadey, "nao igual ao retorno")

    def teste_aumenta_diminui_personagem(self):
        apljogo = AplJogo()
        apljogo.diminui_deslocamento()
        self.assertEqual(-15, apljogo.personagem.velocidadey, "nao igual ao retorno")

    def teste_movimenta_personagem(self):
        apljogo = AplJogo()
        apljogo.aumenta_deslocamento()
        apljogo.movimenta_personagem()
        self.assertEqual(260, apljogo.personagem.posicao.eixoy, "nao igual ao retorno")

    def teste_verifica_qtd_de_vidas(self):
        apljogo = AplJogo()
        apljogo.verifica_qtd_de_vidas()
        self.assertEqual(3, apljogo.personagem.vida, "nao igual ao retorno")


if __name__ == "__main__":
    unittest.main()
