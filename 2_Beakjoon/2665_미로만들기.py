import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    INF = int(1e9)
    movdir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    minBoard = [[INF] * N for _ in range(N)]
    minBoard[0][0] = 0
    q = deque([[0, 0]])

    while q:
        y, x = q.popleft()

        for dy, dx in movdir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                cost = minBoard[y][x]
                if board[ny][nx] == 0:  # 검은 방
                    cost += 1

                if minBoard[ny][nx] > cost:
                    minBoard[ny][nx] = cost
                    q.append([ny, nx])

    print(minBoard[N - 1][N - 1])


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]
    bfs()
