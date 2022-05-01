import sys

input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head

        for s in string:
            if s not in cur_node.child:
                cur_node.child[s] = Node(s)
            cur_node = cur_node.child[s]
        cur_node.data = string

    def search(self, string):
        cur_node = self.head

        for s in string:
            cur_node = cur_node.child[s]

        if cur_node.child:
            return False
        else:
            return True


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        trie = Trie()
        lst = []

        for _ in range(N):
            lst.append(input().rstrip())
            trie.insert(lst[-1])

        flag = True
        lst.sort()
        for l in lst:
            if not trie.search(l):
                flag = False
                break
        if flag:
            print("YES")
        else:
            print("NO")
