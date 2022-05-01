from random import random


class Node:
    def __init__(self, value=None):
        self.value = value
        self.prior = random()
        self.left = None
        self.right = None


def split(root: Node, value: int):
    if root is None:
        return (None, None)
    elif root.value is None:
        return (None, None)
    else:
        if value < root.value:
            left, root.left = split(root.left, value)
            return (left, root)
        else:
            root.right, right = split(root.right, value)
            return (root, right)


def merge(left: Node, right: Node):
    if (not left) or (not right):
        return left or right
    elif left.prior < right.prior:
        left.right = merge(left.right, right)
        return left
    else:
        right.left = merge(left, right.left)
        return right


def insert(root: Node, value: int):
    node = Node(value)
    left, right = split(root, value)
    return merge(merge(left, node), right)


def erase(root: Node, value: int):
    left, right = split(root, value - 1)
    _, right = split(right, value)
    return merge(left, right)


def inorder(root: Node):
    if not root:  # None
        return
    else:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


def interactTreap(root, args):
    """
    Commands:
    + value to add value into treap
    - value to erase all nodes with value

    >>> root = interactTreap(None, "+1")
    >>> inorder(root)
    1
    >>> root = interactTreap(root, "+3 +5 +17 +19 +2 +16 +4 +0")
    >>> inorder(root)
    0 1 2 3 4 5 16 17 19
    >>> root = interactTreap(root, "+4 +4 +4")
    >>> inorder(root)
    0 1 2 3 4 4 4 4 5 16 17 19
    >>> root = interactTreap(root, "-0")
    >>> inorder(root)
    1 2 3 4 4 4 4 5 16 17 19
    >>> root = interactTreap(root, "-4")
    >>> inorder(root)
    1 2 3 5 16 17 19
    >>> root = interactTreap(root, "=0")
    Unknown command
    """
    for arg in args.split():
        if arg[0] == "+":
            root = insert(root, int(arg[1:]))
        elif arg[0] == "-":
            root = erase(root, int(arg[1:]))
        else:
            print("Unkonwn command")
    return root


def main():
    root = None

    args = input()
    while args != "q":
        root = interactTreap(root, args)
        print(root)
        args = input()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
