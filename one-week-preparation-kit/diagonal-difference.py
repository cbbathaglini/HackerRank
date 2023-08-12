def diagonalDifference(arr):
     
    diagonal_principal = []
    diagonal_reversa = []
    reverse = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                diagonal_principal.append(int(arr[i][j]))
    
    arr.reverse()    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                diagonal_reversa.append(int(arr[i][j]))
    #print(f"{abs(sum(diagonal_principal)- sum(diagonal_reversa))}")            
    
    return abs(sum(diagonal_principal)- sum(diagonal_reversa))