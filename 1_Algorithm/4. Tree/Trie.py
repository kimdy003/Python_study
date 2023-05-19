class Node:
    def __init__(self, key, finish=None):
        self.key = key
        self.finish = finish
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curNode = self.head

        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curNode.children:
                curNode.children[char] = Node(char)

            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curNode = curNode.children[char]

        # 문자열이 끝난 지점의 노드의 finish값에 해당 문자열을 표시
        curNode.finish = string

    # 문자열이 존재하는지 탐색
    def search(self, string):
        # 가장 아래에 있는 노드에서부터 탐색 시작한다.
        curNode = self.head

        for char in string:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return False

        # 탐색이 끝난 후에 해당 노드의 finish값이 존재하면
        # 문자가 포함되어있다는 뜻
        if curNode.finish is not None:
            return True
