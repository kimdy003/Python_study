class Node:
    
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def concat(self, L):
        prev = self.tail.prev
        prev.next = L.head.next
        L.head.next.prev = prev
        self.tail = L.tail
        self.nodeCount += L.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    
    def reverse(self):
        result = []
        cur = self.tail
        while cur.prev.prev:
            cur = cur.prev
            result.append(cur.data)
        return result

    
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertBefore(self, next, newNode):
        newNode.next = next
        newNode.prev = next.prev
        
        next.prev.next = newNode
        next.prev = newNode
        
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        cur = prev.next
        prev.next = cur.next
        cur.next.prev = prev
        self.nodeCount -= 1
        return cur.data


    def popBefore(self, next):
        cur = next.prev
        cur.prev.next = next
        next.prev = cur.prev
        self.nodeCount -= 1
        return cur.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        prev = self.getAt(pos -1)     
        return self.popAfter(prev)


def solution(x):
    return 0