#https://www.hackerrank.com/challenges/plus-minus/submissions/code/339025348
def plusMinus(arr):
    len_array = len(arr)
    positivos = 0
    negativos = 0 
    zerados = 0
    for i in range(len_array):
        if arr[i] > 0:
            positivos += 1
        elif arr[i] < 0:
            negativos += 1
        else:
            zerados += 1
    print(f"{positivos/len_array:.6f}") 
    print(f"{negativos/len_array:.6f}") 
    print(f"{zerados/len_array:.6f}") 