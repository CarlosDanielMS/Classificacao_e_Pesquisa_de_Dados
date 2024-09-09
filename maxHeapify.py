def maxHeapify(a, i, n):
    maior = i
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < n and a[l] > a[i]:
        maior = l
    if r < n and a[r] > a[maior]:
        maior = r
    if maior != i:
        a[i], a[maior] = a[maior], a[i]  
        maxHeapify(a, maior, n)

def heapSort(a):
  
    for k in range(len(a) // 2 - 1, -1, -1):
        maxHeapify(a, k, len(a))

    for n in range(len(a) - 1, 0, -1):
        a[0], a[n] = a[n], a[0]
        maxHeapify(a, 0, n)

array = [12, 11, 13, 5, 6, 7]
print("Array original:", array)

heapSort(array)
print("Array ordenado:", array)
