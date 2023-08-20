def insertNodeAtHead(llist, data):
        
    new_llist = SinglyLinkedListNode(data)
   
    if llist is None:
        llist = new_llist
        return llist
    
    else:
        aux = new_llist
        while aux.next is not None:
            aux = aux.next
        aux.next = llist
        
        '''aux_new = new_llist
        while aux_new is not None:
            print(f"-- {aux_new.data}")
            aux_new = aux_new.next'''
                    
    llist = new_llist    
    return llist