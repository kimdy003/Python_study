#
#  20강.py
#  이진 탐색 트리의 원소 삽입 연산 구현
#
#  Create by 김도영 on 2021/04/21
#


class Node:
    
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if self.key > key:
            if self.left == None:
                self.left = Node(key, data)
            else:
                return self.left.insert(key, data)
        
        elif self.key < key:
            if self.right == None:
                self.right = Node(key, data)
            else:
                return self.right.insert(key, data)
        else:
            raise KeyError
            
        return True


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0