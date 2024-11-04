import random
import time

def fibonacci(l, v):
    n = len(l)

    # Inicialização das variáveis de Fibonacci
    Nfib_02 = 0
    Nfib_01 = 1
    Nfib = Nfib_01 + Nfib_02
    
    offset = -1

    # Calcular o número de Fibonacci até que Nfib seja maior que n
    while Nfib < n:
        Nfib_02 = Nfib_01
        Nfib_01 = Nfib
        Nfib = Nfib_01 + Nfib_02

    # Loop principal da busca
    while Nfib > 1:
        i = min(offset + Nfib_02, n - 1)

        if l[i] < v:
            Nfib = Nfib_01
            Nfib_01 = Nfib_02 
            Nfib_02 = Nfib - Nfib_01
            offset = i
            
        elif l[i] > v:
            Nfib = Nfib_02  
            Nfib_01 = Nfib_01 - Nfib_02 
            Nfib_02 = Nfib - Nfib_01
        else:
            return i
    
    # Verificação final
    if Nfib_01 and offset + 1 < n and l[offset + 1] == v:
        return offset + 1

    return -1

# Gerar uma lista ordenada de 10.000 números
lista_ordenada = sorted(random.sample(range(1, 100000), 10000))

# Função para rodar os testes e calcular o desempenho
def teste_desempenho(lista, valor):
    inicio = time.time()
    resultado = fibonacci(lista, valor)
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
print("Média de Tempo - Busca Fibonacci:", media_tempo)

# Exemplo de uso da função
v = 11
resultado = fibonacci(lista_ordenada, v)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado.")
