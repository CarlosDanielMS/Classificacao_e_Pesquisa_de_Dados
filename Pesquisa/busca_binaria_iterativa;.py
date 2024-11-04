def buscaBinaria(lista, valor):
    esquerda = 0 
    direita = len(lista) - 1

    while esquerda < direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


lista = [1,3,5,7,9,11,13,15]
valor = 7 #pesquisa na lista o valor e imprime o indice

resultado = buscaBinaria(lista, valor)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado.")