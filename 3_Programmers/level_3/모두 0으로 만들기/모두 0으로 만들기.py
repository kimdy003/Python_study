import sys

sys.setrecursionlimit(300000)
from collections import defaultdict

answer = 0


def solution(a, edges):
    if sum(a) != 0:
        return -1
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(parent, now):
        global answer
        for nxt in graph[now]:
            if parent != nxt:
                dfs(now, nxt)

        answer += abs(a[now])
        a[parent] += a[now]
        a[now] = 0

    dfs(-1, 0)
    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
