def superDigit(n, k):
    str_n = str(n)    
    len_str_num = len(str_n)
    
    if len_str_num == 1:
        return str_n
    
    soma = 0
    for i in range(len_str_num):
        soma += int(str_n[i])
    
    if k != 0:
        soma = soma * k
        
    return superDigit(soma,0)