import sys
import heapq

input = sys.stdin.readline


def BFS(start):
    dist = [float("inf") for _ in range(N + 1)]
    dist[start] = 0
    q = [[0, start]]

    while q:
        cost, node = heapq.heappop(q)

        for next, sec in graph[node]:
            n_cost = cost + sec
            if dist[next] > n_cost:
                dist[next] = n_cost
                heapq.heappush(q, [n_cost, next])

    print(
        len(dist) - dist.count(float("inf")), max(d for d in dist if d != float("inf"))
    )


test = int(input())
for _ in range(test):
    N, D, C = map(int, input().split())
    graph = {i: [] for i in range(1, N + 1)}

    for _ in range(D):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    BFS(C)
