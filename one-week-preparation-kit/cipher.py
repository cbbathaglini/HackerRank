def caesarCipher(s, k):
    alfabeto = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    str_final = ""
    len_alfabeto = len(alfabeto)
    
    while k > len_alfabeto:
        k -= len_alfabeto
    
    for i in range(len(s)):
        letra = s[i]
        encontrou_letra = False
        if not letra.isnumeric():
            upper = False
            if letra.isupper():
                letra = letra.lower()
                upper = True
            
            for f in range(len_alfabeto):
                posicao = f
                
                if(letra == alfabeto[posicao]):
                    encontrou_letra = True    
                    
                    if( (f+k) >= len_alfabeto):
                        posicao = abs(len_alfabeto - (f+k))
                    else:
                        posicao = f + k
                                
                    print(f"{posicao}")
                    
                    if upper:
                        str_final +=alfabeto[posicao].upper()
                    else:
                        str_final+=alfabeto[posicao]
        
        if not encontrou_letra:
            str_final+=letra
        
        #print(f"{str_final}"

    return str_final
    