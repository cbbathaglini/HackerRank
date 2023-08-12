def lonelyinteger(a):
    
    a.sort()
    lonely = 0
    tam = len(a)
    
    if tam == 1:
        return 1
    
    dictionary_repeated = {i:a.count(i) for i in a}
    for i in dictionary_repeated.items():
        if i[1] == 1:
            return i[0]
