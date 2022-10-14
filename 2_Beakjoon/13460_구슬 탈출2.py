import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
check = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)  # 상 우 하 좌 (시계방향)
q = deque()


def init():
    ry, rx, by, bx = [0] * 4
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                ry, rx = i, j
            elif board[i][j] == "B":
                by, bx = i, j

    q.append((ry, rx, by, bx, 0))
    check[ry][rx][by][bx] = True


def move(y, x, dy, dx, c):
    while board[y + dy][x + dx] != "#" and board[y][x] != "O":
        y, x = y + dy, x + dx
        c += 1
    return y, x, c


def bfs():
    while q:
        ry, rx, by, bx, d = q.popleft()
        if d >= 10:
            break
        for i in range(4):
            nry, nrx, rc = move(ry, rx, dy[i], dx[i], 0)
            nby, nbx, bc = move(by, bx, dy[i], dx[i], 0)

            if board[nby][nbx] == "O":
                continue

            if board[nry][nrx] == "O":
                print(d + 1)
                return

            if nry == nby and nrx == nbx:
                if rc > bc:
                    nry, nrx = nry - dy[i], nrx - dx[i]
                else:
                    nby, nbx = nby - dy[i], nbx - dx[i]

            if not check[nry][nrx][nby][nbx]:
                check[nry][nrx][nby][nbx] = True
                q.append((nry, nrx, nby, nbx, d + 1))
    print(-1)


init()
bfs()
