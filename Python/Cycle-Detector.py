def has_cycle(head):
    if not head or not head.next:
        return 0
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return 1
    
    return 0

#* Check Cycles in LINKED list