import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    visited = [True] * (N + 1)
    visited[start] = False
    q = deque([start])
    cnt = 0

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if visited[nxt]:
                visited[nxt] = False
                q.append(nxt)
                cnt += 1
    return cnt


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(1))
