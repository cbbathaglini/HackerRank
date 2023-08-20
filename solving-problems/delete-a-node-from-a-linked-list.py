def deleteNode(llist, position):
    
    if position == 0:
        llist = llist.next  
    else:
        aux = llist
        position_it = 0    
        while aux.next is not None:
            position_it +=1
            if position_it == position:
                break    
            aux = aux.next
        aux.next = aux.next.next
       
    return llist