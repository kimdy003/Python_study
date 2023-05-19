import sys
from collections import deque

input = sys.stdin.readline


def topologySort():
    result = [0] * (N + 1)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    cnt = 1
    while q:
        cur = len(q)

        for _ in range(cur):
            now = q.popleft()
            result[now] = cnt

            for nxt in graph[now]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        cnt += 1

    for i in result[1:]:
        print(i, end=" ")


if __name__ == "__main__":
    N, M = map(int, input().split())
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    topologySort()
