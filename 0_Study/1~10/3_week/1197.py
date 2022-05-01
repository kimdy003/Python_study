"""
21.10.15
1197_최소 스패닝 트리
"""

import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
graph = []
for _ in range(E):
    a, b, c = map(int, input().split())
    heapq.heappush(graph, (c, a, b))
    heapq.heappush(graph, (c, b, a))


def Find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = Find(parent, parent[x])
    return parent[x]


def Union(parent, a, b):
    a = Find(parent, a)
    b = Find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


ans = 0
while graph:
    c, a, b = heapq.heappop(graph)
    if Find(parent, a) != Find(parent, b):
        Union(parent, a, b)
        ans += c

print(ans)
