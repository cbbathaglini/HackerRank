def insertNodeAtTail(head, data):
    if head is None:
        head = SinglyLinkedListNode(data)
        return head
    
    head_aux = head
    while head_aux.next is not None:
        head_aux = head_aux.next
    head_aux.next = SinglyLinkedListNode(data)
       
    return head
