def angryProfessor(k, a):
    
    no_horario = 0
    atrasados = 0
    for i in range(len(a)):
        if a[i] <= 0 : 
            no_horario += 1
        elif a[i] > 0 : 
            atrasados += 1
    
    if k <= no_horario:
        return "NO"
       
    return "YES"