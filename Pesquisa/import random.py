import random
import time

# Implementação da Busca Binária
def buscaBinaria(lista, valor):
    esquerda = 0
    direita = len(lista) - 1
    comparacoes = 0

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1  # Contando a comparação
        if lista[meio] == valor:
            return meio, comparacoes
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1, comparacoes

# Gerar uma lista ordenada de 10.000 números
lista_ordenada = sorted(random.sample(range(1, 100000), 10000))

# Função para rodar os testes e calcular o desempenho
def teste_desempenho(lista, valor):
    inicio = time.time()
    _, comparacoes = buscaBinaria(lista, valor)
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
print("Média de Comparações - Busca Binária:", media_comparacoes)
print("Média de Tempo - Busca Binária:", media_tempo)

# Questões de Reflexão
print("\nQuestões de Reflexão:")
print("a. Qual método teve o menor número de comparações em média? (Este é apenas o teste da busca binária.)")
print("b. Em quais situações você acha que cada método seria mais apropriado?")
print("c. Como a ordenação da lista afeta a eficiência de cada método?")
