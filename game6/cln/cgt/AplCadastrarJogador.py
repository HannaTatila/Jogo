from cgd.DAOJogador import DAOJogador

_author__ = 'Hanna e Neimar'


class AplCadastrarJogador():

    @staticmethod
    def cadastrar_jogador(ldadosjogador):
        jog = DAOJogador(ldadosjogador)
        if jog.consultar_jogador():
            jog.fechar_banco()
            return False
        else:
            jog.inserir_jogador()
            jog.fechar_banco()
            return True

    @staticmethod
    def validar_login(ldadosjogador):
        jog = DAOJogador(ldadosjogador)
        if jog.validar_login():
            jog.fechar_banco()
            return True
        else:
            return False