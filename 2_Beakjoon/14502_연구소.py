import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# virus = [[i, j] for i in range(N) for j in range(M) if board[i][j] == 2]
dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)
ans = 0


def calculer(_board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if _board[i][j] == 0:
                cnt += 1
    return cnt


def BFS():
    global ans
    q = deque()
    temp = deepcopy(board)
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                q.append([i, j])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and temp[ny][nx] == 0:
                temp[ny][nx] = 2
                q.append([ny, nx])

    ans = max(ans, calculer(temp))


def DFS(cnt):
    if cnt == 3:
        BFS()  # 바이러스 퍼뜨리기
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                DFS(cnt + 1)
                board[i][j] = 0


DFS(0)
print(ans)
