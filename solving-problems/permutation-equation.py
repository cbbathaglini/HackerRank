def permutationEquation(p):
    arr_final = []
    
    for i in range(len(p)):
        arr_final.append(p.index(p.index(i+1)+1)+1)
        
    return arr_final
       