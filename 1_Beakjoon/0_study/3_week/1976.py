"""
21.10.15
1976_여행 가자
"""

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
trip_plan = list(map(int, input().split()))

graph = {}
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            graph[i + 1] = graph.get(i + 1, []) + [j + 1]

start = trip_plan[0]
for next in trip_plan[1:]:
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node == next:
            break

        for nxt in graph[node]:
            queue.append(nxt)
    else:
        print("NO")
        break

    start = next
else:
    print("YES")
