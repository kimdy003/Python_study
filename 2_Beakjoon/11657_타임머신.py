import sys

input = sys.stdin.readline


def bellmanFord():
    dist[1] = 0
    for i in range(1, N + 1):
        for a, b, c in graph:
            if dist[a] == sys.maxsize:
                continue
            if dist[b] > dist[a] + c:
                dist[b] = dist[a] + c

                if i == N:
                    return True
    return False


if __name__ == "__main__":
    dist = [sys.maxsize] * 501
    N, M = map(int, input().split())
    graph = [tuple(map(int, input().split())) for _ in range(M)]
    cycle = bellmanFord()

    if cycle:
        print(-1)
    else:
        for i in range(2, N + 1):
            print(dist[i] if dist[i] != sys.maxsize else -1)
