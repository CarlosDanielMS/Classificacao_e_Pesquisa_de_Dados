def merge(v, ini, meio, fim):
    temp = []
    p1 = ini
    p2 = meio + 1
    tam = fim - ini + 1
    while p1 <= meio and p2 <= fim:
        if v[p1] < v[p2]:
            temp.append(v[p1])
            p1 += 1
        else:
            temp.append(v[p2])
            p2 += 1
    while p1 <= meio:
        temp.append(v[p1])
        p1 += 1
    while p2 <= fim:
        temp.append(v[p2])
        p2 += 1
    v[ini:fim + 1] = temp

def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio + 1, fim)
        merge(v, ini, meio, fim)

# Exemplo de uso:
v = [38, 27, 43, 3, 9, 82, 10]
merge_sort(v, 0, len(v) - 1)
print(v)  # Deve exibir a lista ordenada
