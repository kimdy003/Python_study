import sys

input = sys.stdin.readline

N, M = map(int, input().split())
robot = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]

#    북 동 남 서
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

flag = True
while flag:
    board[robot[0]][robot[1]] = 2  # 현재 위치 청소

    nd = robot[2]
    for i in range(4):
        nd = (nd - 1) % 4
        if i == 1:  # 후진
            back = nd

        ny, nx = robot[0] + dy[nd], robot[1] + dx[nd]
        if board[ny][nx] == 0:
            robot = [ny, nx, nd]
            break
    else:
        ny, nx = robot[0] + dy[back], robot[1] + dx[back]
        if board[ny][nx] != 1:
            robot = [ny, nx, robot[2]]
        else:
            flag = False

cnt = 0
for i in range(N):
    cnt += board[i].count(2)
print(cnt)
