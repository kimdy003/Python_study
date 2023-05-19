import sys
from collections import deque

input = sys.stdin.readline


def calculation(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
    return cnt


def spreadVirus():
    global ans
    q = deque([[i, j] for i in range(N) for j in range(M) if board[i][j] == 2])
    newBoard = [board[i][:] for i in range(N)]

    while q:
        y, x = q.popleft()

        for dy, dx in movdir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and newBoard[ny][nx] == 0:
                newBoard[ny][nx] = 2
                q.append([ny, nx])

    ans = max(ans, calculation(newBoard))


def createWall(cnt):
    if cnt == 3:
        spreadVirus()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                createWall(cnt + 1)
                board[i][j] = 0


if __name__ == "__main__":
    ans = 0
    movdir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]  # 빈 칸 : 0, 벽 : 1, 바이러스 : 2

    createWall(0)
    print(ans)
