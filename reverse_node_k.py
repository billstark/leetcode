class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    counter = 0
    temp = head
    while temp != None:
        counter += 1
        temp = temp.next
    total = int(counter / k)
    if total == 0:
        return head

    h = None
    t = None
    prevH = None
    prevT = None
    current = head

    firstTime = True
    n = k
    count = 0
    while current != None:
        if n == 0:
            if firstTime:
                h = prevH
                firstTime = False
            else:
                t.next = prevH
            t = prevT
            n = k
            prevH = None
            prevT = None
            count += 1
            if count >= total:
                prevH = current
                break
            continue
        temp = current.next
        current.next = prevH
        if prevT == None:
            prevT = current
        prevH = current
        current = temp
        n -= 1

    if firstTime:
        h = prevH
    else:
        t.next = prevH
    return h

head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
head.next = a
a.next = b
b.next = c
c.next = d
result = reverseKGroup(head, 3)
import pdb; pdb.set_trace()
