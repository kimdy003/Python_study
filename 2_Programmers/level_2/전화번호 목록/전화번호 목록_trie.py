class Node(object):
    def __init__(self, key, flag=None):
        self.key = key
        self.flag = flag
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert_search(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(True)
            curr_node = curr_node.children[char]
            if curr_node.flag:
                return False
        curr_node.flag = True
        return True


def solution(phone_book):
    phone_book.sort()
    trie = Trie()
    for phone in phone_book:
        if not trie.insert_search(phone):
            return False
    return True
