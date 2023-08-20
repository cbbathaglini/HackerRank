def reversePrint(llist):
    arr_vals = []
    aux = llist
    while aux is not None:
        arr_vals.append(aux.data)
        aux = aux.next  
  
    while len(arr_vals):
        print(f"{arr_vals.pop()}")