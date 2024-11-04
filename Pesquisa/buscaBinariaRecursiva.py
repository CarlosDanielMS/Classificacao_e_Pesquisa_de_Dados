def buscaBinariaRecursiva(lista, valor, esquerda, direita):
    if esquerda > direita:
        return -1
    
    meio = (esquerda + direita) // 2

    if lista[meio] == valor:
        return meio
    elif lista[meio] > valor:
        return buscaBinariaRecursiva(lista, valor, esquerda, meio -1)
    else:
        return buscaBinariaRecursiva(lista, valor, meio +1, direita)
    

lista = [1,3,5,7,9,11,13,15]

valorBusca = 11

resultado = buscaBinariaRecursiva(lista, valorBusca, 0, len(lista)-1)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado.")