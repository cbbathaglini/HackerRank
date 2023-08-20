import unitttest

def printing(llist):
    print("-------------- PRINTING ARRAY LIST VALUES --------------")
    aux = llist
    while aux is not None:
        print(f"{aux.data}")
        aux = aux.next  
    print("--------------------------------------------------------")


def insertNodeAtPosition(llist, data, position):
    new_value = SinglyLinkedListNode(data)
    
    if position == 0:
        new_value.next = llist
        llist = new_value 
    else:
        position_it = 0
        aux = llist
        while aux is not None:
            position_it +=1
            if position_it == position:
                break   
            aux = aux.next
        new_value.next = aux.next
        aux.next = new_value   
    
    return llist

