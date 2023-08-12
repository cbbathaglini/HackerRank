matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
# output 414


def flippingMatrix(matrix):
    print(f"{matrix}")

    soma_final = 0
    tam = len(matrix)
    for i in range(tam):
        for j in range(tam):
            soma_maxima = 0
            soma_maxima = max(matrix[i][j], soma_maxima)     
            soma_maxima = max(matrix[i][2*int(tam/2)-j-1], soma_maxima)     
            soma_maxima = max(matrix[2*int(tam/2)-i-1][j], soma_maxima)     
            soma_maxima = max(matrix[2*int(tam/2)-i-1][2*int(tam/2)-j-1], soma_maxima)     
            soma_final += soma_maxima
            
    
    return soma_final

soma_maxima = flippingMatrix(matrix)
print(f"Soma max: {soma_maxima}")