import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(a, b):
    q = []
    heapq.heappush(q, (board[a][b], (a, b)))
    dist[a][b] = board[a][b]

    while q:
        rupee, (y, x) = heapq.heappop(q)

        for dy, dx in movdir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if dist[ny][nx] > board[ny][nx] + rupee:
                    dist[ny][nx] = board[ny][nx] + rupee
                    heapq.heappush(q, (dist[ny][nx], (ny, nx)))


if __name__ == "__main__":
    cnt = 1
    while True:
        N = int(input())
        if N == 0:
            break

        board = [list(map(int, input().split())) for _ in range(N)]
        movdir = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # 상, 하, 우, 좌
        dist = [[INF] * N for _ in range(N)]

        dijkstra(0, 0)

        # for i in range(N):
        #     print(dist[i])

        print("Problem {}: {}".format(cnt, dist[N - 1][N - 1]))
        cnt += 1
