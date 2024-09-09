def minHeapify(a, i, n):
    menor = i
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < n and a[l] < a[i]:  
        menor = l
    if r < n and a[r] < a[menor]:
        menor = r
    if menor != i:
        a[i], a[menor] = a[menor], a[i]  
        minHeapify(a, menor, n)
def heapSortMin(a):

    for k in range(len(a) // 2 - 1, -1, -1):
        minHeapify(a, k, len(a))

    for n in range(len(a) - 1, 0, -1):
        a[0], a[n] = a[n], a[0]
        minHeapify(a, 0, n)

array = [12, 11, 13, 5, 6, 7]
print("Array original:", array)

heapSortMin(array)
print("Array ordenado (decrescente):", array)
