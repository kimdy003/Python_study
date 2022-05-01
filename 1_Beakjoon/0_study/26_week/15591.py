import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())
graph = {i: [] for i in range(N + 1)}


def BFS(k, v):
    queue = deque()
    queue.append((v, float("inf")))
    visit = [0] * (N + 1)
    visit[v] = 1
    cnt = 0

    while queue:
        node, min_dist = queue.popleft()
        for next, dist in graph[node]:
            if visit[next]:
                continue

            visit[next] = 1
            if min_dist > dist:
                queue.append((next, dist))
                if dist >= k:
                    cnt += 1
            else:
                queue.append((next, min_dist))
                if min_dist >= k:
                    cnt += 1

    return cnt


for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    print(BFS(k, v))
