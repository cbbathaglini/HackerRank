#https://www.hackerrank.com/challenges/diagonal-difference/submissions/code/339024604
def diagonalDifference(arr):
    len_array = len(arr)
    soma_diagonal_principal = 0
    soma_diagonal_reversa = 0
    diagonal_principal = []
    diagonal_reversa = []
    for i in range(len_array):
        for j in range(len_array):
            if i == j  :
                soma_diagonal_principal += arr[i][j]
                   
            #print(f"i:{i} | j: {j} | array: {arr} | len_array: {len_array}")
                
            if (i==0 and j == (len_array-1)):
                #print(f"caso 1: {arr[i][j]}")
                soma_diagonal_reversa += arr[i][j]
            
            elif (i==(len_array-1) and j == 0):
                #print(f"caso 2: {arr[i][j]}")
                soma_diagonal_reversa += arr[i][j]
            elif j != 0 and i != 0 and j != (len_array-1) and i != (len_array-1) and i == (len_array-1-j):
                #print(f"caso 3: {arr[i][j]}")
                soma_diagonal_reversa += arr[i][j]
            elif len_array % 2 != 0 and i == ((len_array-1)/2) and j == ((len_array-1)/2): #pega o centro
                #print(f"caso 4: {arr[i][j]}")
                soma_diagonal_reversa += arr[i][j]
       
    #print(f"{soma_diagonal_principal}")
    #print(f"{diagonal_reversa}")
    return abs(soma_diagonal_principal-soma_diagonal_reversa)