class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def len(self):
        return self.nodeCount

    def append(self, newNode):
        if self.nodeCount == 0:
            self.head.next = newNode
            self.tail.prev = newNode

            newNode.next = self.tail
            newNode.prev = self.head
            self.nodeCount += 1

        else:
            prev = self.tail.prev
            newNode.next = self.tail
            newNode.prev = prev

            prev.next = newNode
            self.tail.prev = newNode

            self.nodeCount += 1
        return

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def search(self, str):
        idx = 0
        curr = self.head
        while curr.next.next:
            curr = curr.next
            if curr.data == str:
                return idx
            idx += 1

        return idx

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = -1
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

    def insertAt(self, pos, newNode):
        if pos < 0 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        cur = prev.next
        prev.next = cur.next
        cur.next.prev = prev
        self.nodeCount -= 1
        return [prev.data, cur.data]

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


def solution(n, k, cmd):
    doublelist = DoubleLinkedList()

    for i in range(n):
        node = Node(i)
        doublelist.append(node)

    idx = k
    del_node = []
    for c in cmd:

        if len(c) == 1:
            if c == "C":
                del_node.append(doublelist.popAt(idx))
                if idx == doublelist.len():
                    idx -= 1
            else:
                lst = del_node.pop()
                in_pos = doublelist.search(lst[0])

                newnode = Node(lst[1])
                doublelist.insertAt(in_pos, newnode)

                if in_pos <= idx:
                    idx += 1

        else:
            c = c.split()
            if c[0] == "U":
                idx -= int(c[1])

            else:
                idx += int(c[1])

            idx = idx % doublelist.len()

    answer = ""
    r_idx = 0
    ret = doublelist.traverse()
    for n in range(n):
        if n == ret[r_idx]:
            answer += "O"
            r_idx += 1
        else:
            answer += "X"

    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
