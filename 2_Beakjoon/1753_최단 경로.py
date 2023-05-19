import sys
import heapq

input = sys.stdin.readline
INF = 1e9


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for nxt, cost in graph[now]:
            nCost = distance[now] + cost
            if nCost < distance[nxt]:
                distance[nxt] = nCost
                heapq.heappush(q, (nCost, nxt))


if __name__ == "__main__":
    N, M = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dijkstra(start)

    for i in range(1, N + 1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])
