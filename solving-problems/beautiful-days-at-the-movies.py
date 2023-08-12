def beautifulDays(i, j, k):
    
    beautiful_days = 0
    while i <= j:
        '''    
        print(f"abs({i} - int({str(i)[::-1]}))/{k} =>")
        print(f"abs({i} - {int(str(i)[::-1])})/{k} =>")
        print(f"abs({i - int(str(i)[::-1])})/{k} =>")
        print(f"{abs(i - int(str(i)[::-1]))}/{k} =>")
        print(f"Resultado: {abs(i - int(str(i)[::-1]))/k}")
        print(f"--")
        '''
        
        division = abs(i - int(str(i)[::-1]))/k
        split_div = str(division).split(".0")
        if len(split_div) > 1 and split_div[1] == '':
            beautiful_days +=1
        i+=1
       
    return beautiful_days