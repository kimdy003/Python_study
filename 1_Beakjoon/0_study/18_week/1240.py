import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


for _ in range(M):
    a, b = map(int, input().split())

    def bfs(start, end):
        queue = deque()
        queue.append(start)
        visit = [-1] * (N + 1)
        visit[start] = 0

        while queue:
            node = queue.popleft()
            if node == end:
                break
            for next in graph[node]:
                if visit[next[0]] == -1:
                    visit[next[0]] = visit[node] + next[1]
                    queue.append(next[0])
        return visit[end]

    print(bfs(a, b))
