def fibonacci(l, v):
    n = len(l)

    Nfib_02 = 0
    Nfib_01 = 1
    Nfib = Nfib_01 + Nfib_02
    
    offset = -1

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
    
    if Nfib_01 and offset + 1 < n and l(offset + 1) == v:
        return offset + 1

    return -1


l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
v = 11

resultado = fibonacci(l, v)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado.")
