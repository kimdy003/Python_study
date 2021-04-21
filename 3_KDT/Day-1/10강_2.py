# 
#  10강_2.py
#  양방향 연결 리스트 노드 삽입
#
#  Created by 김도영 on 2021/04/20.
#

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


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def insertBefore(self, next, newNode):
        newNode.next = next
        newNode.prev = next.prev
        
        next.prev.next = newNode
        next.prev = newNode
        
        self.nodeCount += 1
        return True


def solution(x):
    return 0