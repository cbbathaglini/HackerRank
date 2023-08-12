def countingSort(arr):
    arr_return = []
    
    for i in range(len(arr)):
        contador = 0
        for j in range(len(arr)):
            if arr[j] == i:
                contador+=1
        arr_return.append(contador) 
        if len(arr_return) == 100:
            break
    
    return arr_return