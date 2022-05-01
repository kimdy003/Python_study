"""
21.10.15
1717_집합의 표현
"""

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
N, M = map(int, input().split())
parent = [i for i in range(N + 1)]


def Find(parent, x):
    if parent[x] == x:
        return x
    # 재귀 없이 코드 짜는법 생각해보기
    parent[x] = Find(parent, parent[x])
    return parent[x]


def Union(parent, a, b):
    a = Find(parent, a)
    b = Find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    order, node1, node2 = map(int, input().split())

    if order == 0:  # 합집합
        Union(parent, node1, node2)

    else:  # 검사해서 출력
        if Find(parent, node1) != Find(parent, node2):
            print("NO")
        else:
            print("YES")
