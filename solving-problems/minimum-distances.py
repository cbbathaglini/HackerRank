def minimumDistances(a):
    vals = []
    invalid = 0
    for i in range(len(a)-1):
        if a[i] in a[i+1:]:
            posi = a[i+1:].index(a[i]) + (i+1) 
            vals.append( abs(i - posi))
        else:
            invalid+=1
    if invalid == len(a)-1:
        return -1

    return min(vals)