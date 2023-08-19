def circularArrayRotation(a, k, queries):

    n = len(a)
    arr_aux = []

    for i in range(k):
        a.insert(0,a[n-1])
        a.pop()
        
    for i in range(len(queries)):
        arr_aux.append(a[queries[i]])
    return arr_aux