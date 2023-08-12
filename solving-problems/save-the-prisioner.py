def saveThePrisoner(n, m, s):

    choosen = (m - (int(m/n) * n)) - 1
    
    if choosen == 0 and s>1 and choosen == -1: 
        return s
    if s + choosen > n:
        return (s + choosen) - n  
    if choosen == -1 and s == 1:
        return n
    
    return s + choosen