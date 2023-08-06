#https://www.hackerrank.com/challenges/migratory-birds/submissions/code/339494126
def migratoryBirds(arr):
    arr_frequencies = []
    arr_numbers = []
    arr.sort()
    for i in range(len(arr)):
        contador = 0
        if arr[i] not in arr_numbers:
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    contador += 1
                    if arr[i] not in arr_numbers:
                        arr_numbers.append(arr[i])
            arr_frequencies.append(contador)
    
    maior = 0
    index=-1
    for i in range(len(arr_frequencies)):
        if arr_frequencies[i] > maior:
            maior = arr_frequencies[i]
            index = i
    #print(f"--{index}")      
    #print(f"{arr_numbers}")
    #print(f"{arr_frequencies}")
    #print(f"{arr_numbers[index]}")
    return arr_numbers[index]
