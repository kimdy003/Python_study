import sys
from collections import deque

input = sys.stdin.readline

N, M, y, x, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dice = [0] * 7
dy, dx = (0, 0, 0, -1, 1), (0, 1, -1, 0, 0)  # 동(1), 서(2), 북(3), 남(4)


def switchDice(d):
    if d == 1:  # 동쪽으로 이동
        dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]

    elif d == 2:  # 서쪽으로 이동
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]

    elif d == 3:  # 북쪽으로 이동
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]

    elif d == 4:  # 남쪽으로 이동
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]


def solve():
    global y, x

    for d in list(map(int, input().split())):
        ny, nx = y + dy[d], x + dx[d]
        if ny < 0 or N <= ny or nx < 0 or M <= nx:
            continue

        switchDice(d)

        if board[ny][nx] == 0:
            board[ny][nx] = dice[6]
        else:
            dice[6] = board[ny][nx]
            board[ny][nx] = 0

        print(dice[1])
        y, x = ny, nx

    return


solve()
