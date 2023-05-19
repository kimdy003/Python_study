# O(VE)

import sys

input = sys.stdin.readline
INF = int(1e9)


def bellmanFord(start):
    dist[start] = 0  # start = 1
    for i in range(N):  # 정점 수만큼 반복, 반복수
        for cur, nxt, cost in graph:
            if dist[cur] == INF:
                continue
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost

                if i == N - 1:  # N-1(=v-1)번 이후 반복에도 값이 갱신되면 음수 순환 존재
                    return True
    return False


if __name__ == "__main__":
    N, M = map(int, input().split())  # N : node, M : edge
    graph = [tuple(map(int, input().split())) for _ in range(M)]
    dist = [INF] * N
    cycle = bellmanFord(1)

    if cycle:
        print(-1)
    else:
        for i in range(2, N + 1):
            print(dist[i] if dist[i] != INF else -1)
