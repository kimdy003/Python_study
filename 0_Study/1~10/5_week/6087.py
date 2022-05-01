"""
2021.11.06
6087_레이저 통신
"""
import sys
from collections import deque

input = sys.stdin.readline
movdir = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 동 남 서 북

M, N = map(int, input().split())
board = [[0] * M for _ in range(N)]
point = []

for i in range(N):
    for j, s in enumerate(input().rstrip()):
        if s == "C":
            board[i][j] = 1
            point.append([i, j])
        elif s == "*":
            board[i][j] = -1
        else:
            board[i][j] = 0


def rotation(y, x, d, mirror, q):
    nd = [(d + 1) % 4, (d + 3) % 4]
    for i in nd:
        if mirror[y][x][i] == 0 or mirror[y][x][i] > mirror[y][x][d] + 1:
            mirror[y][x][i] = mirror[y][x][d] + 1
            q.append([y, x, i])


def bfs():
    mirror = [[[0] * 4 for _ in range(M)] for _ in range(N)]
    q = deque()
    sy, sx = point[0]
    ey, ex = point[1]

    for d in range(4):
        q.append([sy, sx, d])  # 좌표, 방향
    mirror[sy][sx] = [1, 1, 1, 1]  # 나중에 -1 해야함

    ans = []
    while q:
        y, x, d = q.popleft()

        ny, nx = y + movdir[d][0], x + movdir[d][1]
        if 0 <= ny < N and 0 <= nx < M:
            if mirror[ny][nx][d] == 0 or mirror[ny][nx][d] > mirror[y][x][d]:
                if board[ny][nx] == 0:
                    mirror[ny][nx][d] = mirror[y][x][d]
                    q.append([ny, nx, d])
                    rotation(ny, nx, d, mirror, q)

                elif ny == ey and nx == ex:
                    mirror[ny][nx][d] = mirror[y][x][d]
                    ans.append(mirror[ny][nx][d])

    print(min(ans) - 1)


bfs()
