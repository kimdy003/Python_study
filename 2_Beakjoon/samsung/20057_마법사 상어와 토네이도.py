import sys

input = sys.stdin.readline


def sandMove(y, x, direction, board):
    global ans

    # 3. alpha, 떨어지는 모래 구하기
    total = 0
    for dy, dx, z in direction:
        ny, nx = y + dy, x + dx

        # y의 모래 기준 비율 구하기
        if z == 0:  # alpha 구하기. 순서상 맨 마지막에 온다
            newSand = board[y][x] - total
        else:
            newSand = int(board[y][x] * z)
            total += newSand

        # 각 해당 위치 모래 증가
        if 0 <= ny < N and 0 <= nx < N:
            board[ny][nx] += newSand
        else:
            ans += newSand
    board[y][x] = 0
    print()
    for i in range(N):
        print(board[i])


def solution():
    movdir = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 좌 하 우 상
    board = [list(map(int, input().split())) for _ in range(N)]

    y = x = N // 2
    depth = 1
    dir = 0

    cnt = 0
    while y > -1 and x > -1:
        ny, nx = y + movdir[dir][0], x + movdir[dir][1]
        sandMove(ny, nx, dict[dir], board)

        y, x = ny, nx
        cnt += 1

        if cnt == depth:
            if dir in [1, 3]:
                depth += 1
            dir = (dir + 1) % 4
            cnt = 0


if __name__ == "__main__":
    ans = 0
    N = int(input())
    # 2. 방향별 모래 비율 위치
    left = [
        (1, 1, 0.01),
        (-1, 1, 0.01),
        (1, 0, 0.07),
        (-1, 0, 0.07),
        (1, -1, 0.1),
        (-1, -1, 0.1),
        (2, 0, 0.02),
        (-2, 0, 0.02),
        (0, -2, 0.05),
        (0, -1, 0),
    ]
    right = [(y, -x, z) for y, x, z in left]
    down = [(-x, y, z) for y, x, z in left]
    up = [(x, y, z) for y, x, z in left]

    # 1.토네이도 회전 방향(y위치)
    dict = {0: left, 1: down, 2: right, 3: up}

    solution()
    print(ans)
