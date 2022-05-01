import time
import random
import sys

sys.setrecursionlimit(10 ** 6)


def solution(board):
    start = time.time()
    board = [
        [random.randint(-10000, 10000) for _ in range(1000)]
        for _ in range(1000)
    ]
    N = len(board)

    Max = 0
    movdir = [[0, 1], [1, 0]]

    def dfs(y, x, weight):
        nonlocal Max
        if y == N - 1 and x == N - 1:
            if Max < weight:
                Max = weight
            return

        for dy, dx in movdir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] == 0:
                    dfs(ny, nx, weight)
                    dfs(ny, nx, -weight)
                else:
                    dfs(ny, nx, weight + board[ny][nx])

    dfs(0, 0, board[0][0])
    end = time.time()
    print(f"{end - start:.5f} sec")

    return Max


print(solution([[-10, 20, 30], [-10, 0, 10], [-20, 40, 1]]))
