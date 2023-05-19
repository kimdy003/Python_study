# O(E logV)

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작 노드로 가지 위한 경로는 0으로 설정, 큐에 삽입
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # dist에 어느 값을 더해도 distance[now]보다 크기 때문에 밑에 for문을 수행할 필요가 없다.
        if distance[now] < dist:
            continue

        for nxt, c in graph[now]:
            cost = dist + c
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))


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
            print("INFINITY")
        else:
            print(distance[i])
