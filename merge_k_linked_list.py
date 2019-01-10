class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Heap:

    def __init__(self):
        self.data = []

    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp

    def leftChild(self, i):
        return i * 2 + 1

    def rightChild(self, i):
        return i * 2 + 2
    
    def parent(self, i):
        return int((i + 1) / 2) - 1

    def swimUp(self, i):
        parent = self.parent(i)
        while self.data[parent][0] > self.data[i][0] and i != 0:
            self.swap(parent, i)
            i = parent
            parent = self.parent(i)

    def swimDown(self, i):
        leftChild = self.leftChild(i)
        rightChild = self.rightChild(i)

        largestHasChild = self.parent(len(self.data) - 1)
        while i <= largestHasChild:
            if rightChild < len(self.data):
                if self.data[i][0] > self.data[leftChild][0] and self.data[i][0] <= self.data[rightChild][0]:
                    self.swap(i, leftChild)
                    i = leftChild
                    leftChild = self.leftChild(i)
                    rightChild = self.rightChild(i)
                    continue
                if self.data[i][0] > self.data[rightChild][0] and self.data[i][0] <= self.data[leftChild][0]:
                    self.swap(i, rightChild)
                    i = rightChild
                    leftChild = self.leftChild(i)
                    rightChild = self.rightChild(i)
                    continue
                if self.data[i][0] > self.data[leftChild][0] and self.data[i][0] > self.data[rightChild][0] and self.data[leftChild][0] <= self.data[rightChild][0]:
                    self.swap(i, leftChild)
                    i = leftChild
                    leftChild = self.leftChild(i)
                    rightChild = self.rightChild(i)
                    continue
                if self.data[i][0] > self.data[leftChild][0] and self.data[i][0] > self.data[rightChild][0] and self.data[leftChild][0] > self.data[rightChild][0]:
                    self.swap(i, rightChild)
                    i = rightChild
                    leftChild = self.leftChild(i)
                    rightChild = self.rightChild(i)
                    continue
                break
            if self.data[i][0] > self.data[leftChild][0]:
                self.swap(i, leftChild)
                i = leftChild
                leftChild = self.leftChild(i)
                rightChild = self.rightChild(i)
                continue
            break

    def push(self, item):
        self.data.append(item)
        self.swimUp(len(self.data) - 1)

    def pop(self):
        result = self.data[0]
        self.swap(0, len(self.data) - 1)
        self.data = self.data[:-1]
        self.swimDown(0)
        return result

def mergeKLists(lists):
    lists = [x for x in lists if x != None]
    finished = 0
    head = ListNode(-1)
    pointer = head

    heap = Heap()
    for idx, l in enumerate(lists):
        heap.push((l.val, idx))
        lists[idx] = lists[idx].next

    import pdb; pdb.set_trace()
    while finished != len(lists):
        nextNode = heap.pop()
        nextResult = ListNode(nextNode[0])
        pointer.next = nextResult
        pointer = pointer.next

        nextIndex = nextNode[1]
        if lists[nextIndex] != None:
            heap.push((lists[nextIndex].val, nextIndex))
            lists[nextIndex] = lists[nextIndex].next
        else:
            finished += 1

    while len(heap.data) != 0:
        nextNode = heap.pop()
        nextResult = ListNode(nextNode[0])
        pointer.next = nextResult
        pointer = pointer.next

    return head.next

lst1 = ListNode(1)
head2 = ListNode(4)
head3 = ListNode(5)
lst2 = ListNode(1)
head4 = ListNode(3)
head5 = ListNode(4)
lst3 = ListNode(2)
head6 = ListNode(6)
lst1.next = head2
head2.next = head3
lst2.next = head4
head4.next = head5
lst3.next = head6

result = mergeKLists([lst1, lst2, lst3])
import pdb; pdb.set_trace()
print(result)