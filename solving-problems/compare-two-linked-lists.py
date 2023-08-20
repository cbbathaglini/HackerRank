def compare_lists(llist1, llist2):
    aux_l1, aux_l2 = llist1, llist2
    equals = 1
    while aux_l1 is not None or aux_l2 is not None:
        if (aux_l1 is None  or  aux_l2 is None) or aux_l1.data != aux_l2.data: 
            equals = 0
            break
        aux_l1 = aux_l1.next
        aux_l2 = aux_l2.next
    return equals