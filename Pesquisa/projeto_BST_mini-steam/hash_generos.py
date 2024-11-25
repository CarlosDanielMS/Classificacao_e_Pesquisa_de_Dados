class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = {}

    def adicionar_jogo(self, jogo):
        #Adiciona um jogo à tabela hash com base nos gêneros.
        for genero in jogo.generos:
            if genero not in self.genero_para_jogos:
                self.genero_para_jogos[genero] = []
            self.genero_para_jogos[genero].append(jogo.jogo_id)

    def obter_jogos(self, genero):
        #Busca jogos de um determinado gênero
        return self.genero_para_jogos.get(genero, [])
