import math
import random
import time

# Implementação do Jump Search
def jumpSearch(l, v):
    n = len(l)
    passo = int(math.sqrt(n))
    anterior = 0

    while l[min(passo, n) - 1] < v:
        anterior = passo
        passo += int(math.sqrt(n))
        if anterior >= n:
            return -1
    
    for i in range(anterior, min(passo, n)):
        if l[i] == v:
            return i
    return -1

# Gerar uma lista ordenada de 10.000 números
lista_ordenada = sorted(random.sample(range(1, 100000), 10000))

# Função para rodar os testes e calcular o desempenho
def teste_desempenho(lista, valor):
    inicio = time.time()
    resultado = jumpSearch(lista, valor)
    tempo = time.time() - inicio
    return resultado, tempo

# Executar múltiplos testes e calcular a média de tempo
resultados = []
for _ in range(100):  # Rodando o teste 100 vezes
    valor_buscado = random.choice(lista_ordenada)
    resultado, tempo = teste_desempenho(lista_ordenada, valor_buscado)
    resultados.append(tempo)

# Calculando a média
media_tempo = sum(resultados) / len(resultados)

# Resultados Finais
print("Média de Tempo - Jump Search:", media_tempo)

# Exemplo de uso da função
v = 13
resultado = jumpSearch(lista_ordenada, v)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado.")
