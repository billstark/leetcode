class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    if head == None:
        return head

    if head.next == None:
        return head

    current = head
    nextHead = head.next
    swapped = swapPairs(nextHead.next)
    current.next = swapped
    nextHead.next = current
    return nextHead

head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
head.next = a
a.next = b
b.next = c
import pdb; pdb.set_trace()
result = swapPairs(head)
import pdb; pdb.set_trace()