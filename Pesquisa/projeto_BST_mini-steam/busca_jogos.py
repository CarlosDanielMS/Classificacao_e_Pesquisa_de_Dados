from arvore_jogos import ArvoreJogos
from hash_generos import HashGeneros

class MotorBuscaJogos:
    def __init__(self):
        self.catalogo_jogos = ArvoreJogos()
        self.generos = HashGeneros()

    def adicionar_jogo(self, jogo):
        self.catalogo_jogos.inserir(jogo)
        self.generos.adicionar_jogo(jogo)

    def buscar_por_preco(self, preco):
        return self.catalogo_jogos.buscar_por_preco(preco)

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        return self.catalogo_jogos.busca_por_faixa_preco(preco_minimo, preco_maximo)

    def buscar_por_genero(self, genero):
        return self.generos.obter_jogos(genero)
