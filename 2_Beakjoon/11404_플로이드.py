import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        graph[i][i] = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] == sys.maxsize:
                graph[i][j] = 0

        print(*graph[i][1:])
