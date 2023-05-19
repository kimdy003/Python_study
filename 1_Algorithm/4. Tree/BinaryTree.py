class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root: Node, data: int):
        if root is None:
            root = Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    # Search
    def Search(self, root: Node, key: int):
        if root is None or root.data is key:
            return root
        elif key < root.data:
            return self.Search(root.left, key)
        elif key > root.data:
            return self.Search(root.right, key)

    # 전위 순회
    def PreOrder(self, root: Node):
        if root is None:
            pass
        else:
            print(root.data)
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    # 중위 순회
    def InOrder(self, root: Node):
        if root is None:
            pass
        else:
            self.InOrder(root.left)
            print(root.data)
            self.InOrder(root.right)

    # 후위 순회
    def PostOrder(self, root: Node):
        if root is None:
            pass
        else:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.data)

    # 레벨 순회
    def LevelOrder(self, root: Node):
        from collections import deque

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            print(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
