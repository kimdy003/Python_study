import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = {i: [] for i in range(1, N + 1)}

for i in range(1, N + 1):
    lst = list(map(int, input().split()))[:-1]
    for j in range(1, len(lst), 2):
        graph[lst[0]].append([lst[j], lst[j + 1]])


def bfs(start):
    visit = [-1] * (N + 1)
    q = deque()
    q.append(start)
    visit[start] = 0
    ret = [0, 0]

    while q:
        node = q.popleft()

        for next, weight in graph[node]:
            if visit[next] == -1:
                visit[next] = visit[node] + weight
                q.append(next)
                if ret[0] < visit[next]:
                    ret = visit[next], next
    return ret


dis, node = bfs(1)
ans, node = bfs(node)
print(ans)
