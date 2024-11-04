import random
import time

# Implementação da Busca Binária Recursiva
def buscaBinariaRecursiva(lista, valor, esquerda, direita, comparacoes):
    if esquerda > direita:
        return -1, comparacoes
    
    meio = (esquerda + direita) // 2
    comparacoes += 1  # Contando a comparação

    if lista[meio] == valor:
        return meio, comparacoes
    elif lista[meio] > valor:
        return buscaBinariaRecursiva(lista, valor, esquerda, meio - 1, comparacoes)
    else:
        return buscaBinariaRecursiva(lista, valor, meio + 1, direita, comparacoes)

# Gerar uma lista ordenada de 10.000 números
lista_ordenada = sorted(random.sample(range(1, 100000), 10000))

# Função para rodar os testes e calcular o desempenho
def teste_desempenho(lista, valor):
    inicio = time.time()
    _, comparacoes = buscaBinariaRecursiva(lista, valor, 0, len(lista) - 1, 0)
    tempo = time.time() - inicio
    return comparacoes, tempo

# Executar múltiplos testes e calcular a média de comparações
resultados = []
for _ in range(100):  # Rodando o teste 100 vezes
    valor_buscado = random.choice(lista_ordenada)
    resultados.append(teste_desempenho(lista_ordenada, valor_buscado))

# Calculando as médias
media_comparacoes = sum([x[0] for x in resultados]) / len(resultados)
media_tempo = sum([x[1] for x in resultados]) / len(resultados)

# Resultados Finais
print("Média de Comparações - Busca Binária Recursiva:", media_comparacoes)
print("Média de Tempo - Busca Binária Recursiva:", media_tempo)

# Exemplo de uso da função
valorBusca = 11
resultado, comparacoes = buscaBinariaRecursiva(lista_ordenada, valorBusca, 0, len(lista_ordenada) - 1, 0)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado.")
