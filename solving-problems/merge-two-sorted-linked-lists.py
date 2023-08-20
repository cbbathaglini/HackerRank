def mergeLists(head1, head2):
    new_llist = None
    aux_h1, aux_h2 = head1, head2
    while aux_h1 is not None and aux_h2 is not None:
        if aux_h1.data == aux_h2.data:
            new_llist  = insertNodeAtTail(new_llist, aux_h1.data)
            new_llist  = insertNodeAtTail(new_llist, aux_h2.data)
            aux_h1 = aux_h1.next
            aux_h2 = aux_h2.next
        
        elif aux_h1.data < aux_h2.data:
            new_llist  = insertNodeAtTail(new_llist, aux_h1.data)
            aux_h1 = aux_h1.next

        elif aux_h1.data > aux_h2.data:
            new_llist  = insertNodeAtTail(new_llist, aux_h2.data)
            aux_h2 = aux_h2.next
                
    if aux_h1 is None:
        while aux_h2 is not None:
            new_llist = insertNodeAtTail(new_llist, aux_h2.data)
            aux_h2 = aux_h2.next
        
    if aux_h2 is None:
        while aux_h1 is not None:
            new_llist = insertNodeAtTail(new_llist, aux_h1.data)
            aux_h1 = aux_h1.next
     
    
    return new_llist  