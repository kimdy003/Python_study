class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self) -> None:
        self.root = None

    def _height(self, node: Node):
        if node == None:
            return 0
        return node.height

    # bf 계산
    def bf(self, node: Node):
        if node == None:
            return 0
        return self._height(node.left) - self._height(node.right)

    # 불균형 처리
    def balance(self, node: Node):
        if self.bf(node) > 1:  # node의 왼쪽 서브트리가 높아서 불균형 발생
            if self.bf(node.left) < 0:  # node의 왼쪽 자식의 오른쪽 서브트리가 높은 경우: "<" 모양
                node.left = self.rotateLeft(node.left)  # LR 회전
            node = self.rotateRight(node)

        elif self.bf(node) < -1:  # node의 오른쪽 서브트리가 높아서 불균형 발생
            if self.bf(node.right) > 0:  # node의 오른쪽자식의 왼쪽 서브트리가 높은 경우: ">" 모양
                node.right = self.rotateRight(node.right)  # RL 회전
            node = self.rotateLeft(node)  # RR 회전

        return node

    def rotateRight(self, node: Node):
        x: Node = node.left
        node.left = x.right
        x.right = node

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        return x  # 회전 후 x가 node의 이전 자리로 이동했으므로 x를 return

    def rotateLeft(self, node: Node):
        x: Node = node.right
        node.right = x.left
        x.left = node

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        return x  # 회전 후 x가 node의 이전 자리로 이동했으므로 x를 return

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node: Node, val):
        if node == None:
            return Node(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return self.balance(node)  # node의 균형 점검 및 불균형 처리

    def minimum(self, node: Node):  # 현재 node에서 최소값 찾기(이진노드이므로 왼쪽으로만 가면 됨)
        while node.left:
            node = node.left
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node: Node, val):
        if node == None:
            return None

        if val < node.val:  # 왼쪽 자식으로 이동
            node.left = self._delete(node.left, val)
        elif node.val < val:  # 오른쪽 자식으로 이동
            node.right = self._delete(node.right, val)
        else:  # 삭제할 노드 발견
            # 노드에 자식이 하나만 있는 경우
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right

            # 자식이 두개 있는 경우
            minNode = self.minimum(node.right)
            node.val = minNode.val
            node.right = self._delete(node.right, minNode.val)

        if node == None:
            return None

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return self.balance(node)  # node의 균형 점검 및 불균형 처리

    def preorder(self, node: Node):
        if node == None:
            return

        print(node.val, end=" ")
        print("down left: ", end=" ")
        self.preorder(node.left)
        print("returned;", end="\n")
        print("down right: ", end=" ")
        self.preorder(node.right)
        print("returned;", end=" ")

    def inorder(self, node: Node):
        if node.left:
            self.inorder(node.left)

        print(str(node.val), " ", end="")

        if node.right:
            self.inorder(node.right)


tree = AVL()
tree.insert(3)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(9)
tree.insert(17)
tree.insert(22)
tree.insert(-3)
tree.delete(3)
tree.preorder(tree.root)
