import os

_author__ = 'Hanna e Neimar'


class CaminhoRecursos:
    @staticmethod
    def caminho_imagens():
        return (os.path.dirname(os.path.realpath(__file__))).replace("principal", os.path.join("recursos", "imagem"))

    @staticmethod
    def caminho_arquivos():
        return (os.path.dirname(os.path.realpath(__file__))).replace("principal", os.path.join("recursos", "arquivo"))

    @staticmethod
    def caminho_imagens_obstaculos():
        return (os.path.dirname(os.path.realpath(__file__))).replace("principal",
                                                                     os.path.join("recursos\\imagem", "obstaculos"))

    @staticmethod
    def caminho_imagens_obstaculosedu():
        return (os.path.dirname(os.path.realpath(__file__))).replace("principal",
                                                                     os.path.join("recursos\\imagem", "obstaculosedu"))

    @staticmethod
    def caminho_musicas():
        return (os.path.dirname(os.path.realpath(__file__))).replace("principal",
                                                                     os.path.join("recursos\\audio", "musica"))

    @staticmethod
    def caminho_sons():
        return (os.path.dirname(os.path.realpath(__file__))).replace("principal",
                                                                     os.path.join("recursos\\audio", "sons"))