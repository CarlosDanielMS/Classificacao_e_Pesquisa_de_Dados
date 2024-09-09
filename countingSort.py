def countingSort(arr):
   
    max_val = max(arr)
    
    
    count = [0] * (max_val + 1)
    
    
    for num in arr:
        count[num] += 1
    
    
    sorted_index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1
            count[i] -= 1

array = [4, 2, 2, 8, 3, 3, 1]
print("Array original:", array)

countingSort(array)
print("Array ordenado:", array)
