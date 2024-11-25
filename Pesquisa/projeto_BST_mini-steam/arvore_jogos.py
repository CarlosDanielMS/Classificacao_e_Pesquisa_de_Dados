class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

class ArvoreJogos:
    def __init__(self):
        self.raiz = None



    #### INSERIR USANDO RECURSIVIDADE
    def inserir(self, jogo):
        novo_no = NoJogo(jogo)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, atual, novo_no):
        if novo_no.jogo.preco < atual.jogo.preco:
            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self._inserir_recursivo(atual.esquerda, novo_no)
        else:
            if atual.direita is None:
                atual.direita = novo_no
            else:
                self._inserir_recursivo(atual.direita, novo_no)



    ####  BUSCA RECURSIVA POR PREÇO SOMENTE
    def buscar_por_preco(self, preco):
        return self._buscar_recursivo(self.raiz, preco)

    def _buscar_recursivo(self, atual, preco):
        if atual is None:
            return []
        if atual.jogo.preco == preco:
            return [atual.jogo]
        elif preco < atual.jogo.preco:
            return self._buscar_recursivo(atual.esquerda, preco)
        else:
            return self._buscar_recursivo(atual.direita, preco)



    #### BUSCA RECURSIVA POR FAIXA MIN E MAX
    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        resultados = []
        self._buscar_faixa_recursivo(self.raiz, preco_minimo, preco_maximo, resultados)
        return resultados

    def _buscar_faixa_recursivo(self, atual, preco_minimo, preco_maximo, resultados):
        if atual is not None:
            if preco_minimo <= atual.jogo.preco <= preco_maximo:
                resultados.append(atual.jogo)
            if preco_minimo < atual.jogo.preco:
                self._buscar_faixa_recursivo(atual.esquerda, preco_minimo, preco_maximo, resultados)
            if atual.jogo.preco < preco_maximo:
                self._buscar_faixa_recursivo(atual.direita, preco_minimo, preco_maximo, resultados)
