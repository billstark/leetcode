class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    start = head
    end = head
    for i in range(n):
        end = end.next

    while end.next != None:
        start = start.next
        end = end.next

    start.next = start.next.next

    return head

head = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

head.next = b
b.next = c
c.next = d
d.next = e

removeNthFromEnd(head, 2)

import pdb; pdb.set_trace()