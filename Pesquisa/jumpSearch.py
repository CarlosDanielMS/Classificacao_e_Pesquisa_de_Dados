import math

def jumpSearch(l, v):
    n = len(l)
    passo = int(math.sqrt(n))
    anterior = 0

    while l[min(passo, n)- 1] < v:
        anterior = passo
        passo += int(math.sqrt(n))
        if anterior >= n:
            return -1
    for i in range(anterior, min(passo, n)):
        if l[i] == v:
            return i
    return -1

l = [1,3,5,7,9,11,13,15,17,19]
v = 13

resultado = jumpSearch(l, v)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado.")