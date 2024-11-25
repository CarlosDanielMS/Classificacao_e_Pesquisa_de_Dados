class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos  # Lista de gêneros

    def __repr__(self):
        return f"Jogo(ID={self.jogo_id}, Título='{self.titulo}', Preço=R${self.preco}, Gêneros={self.generos})"
