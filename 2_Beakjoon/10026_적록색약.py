import sys
from collections import deque

input = sys.stdin.readline


def bfs(i, j, visited):
    movdir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = deque([[i, j]])
    pivot = board[i][j]

    while q:
        y, x = q.popleft()

        for dy, dx in movdir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == False and board[ny][nx] == pivot:
                    visited[ny][nx] = True
                    q.append([ny, nx])


if __name__ == "__main__":
    ans = [0, 0]
    N = int(input())
    board = [[c for c in input().strip()] for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                bfs(i, j, visited)
                ans[0] += 1

    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == "G":
                board[i][j] = "R"

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                bfs(i, j, visited)
                ans[1] += 1

    print(*ans)
