class HashGeneros:
    def __init__(self, tamanho=10):
        # Inicializa a tabela hash com um tamanho fixo.
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]  # Lista de listas para lidar com colisões.

    def _funcao_hash(self, genero):
        # Calcula o índice na tabela hash para um determinado gênero.
        return hash(genero) % self.tamanho

    def adicionar_jogo(self, jogo):
        # Adiciona um jogo à tabela hash com base nos gêneros.
        for genero in jogo.generos:
            indice = self._funcao_hash(genero)
            for item in self.tabela[indice]:
                if item['genero'] == genero:
                    item['jogos'].append(jogo.jogo_id)
                    break
            else:
                # Adiciona um novo gênero se não existir
                self.tabela[indice].append({'genero': genero, 'jogos': [jogo.jogo_id]})

    def obter_jogos(self, genero):
        # Busca jogos de um determinado gênero.
        indice = self._funcao_hash(genero)
        for item in self.tabela[indice]:
            if item['genero'] == genero:
                return item['jogos']
        return []  # Retorna uma lista vazia se o gênero não for encontrado.

