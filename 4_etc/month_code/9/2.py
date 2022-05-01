import sys

sys.setrecursionlimit(10 ** 3)
movdir = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상우하좌


def right(dir):
    return dir + 1 if dir < 3 else 0


def left(dir):
    return dir - 1 if dir > 0 else 3


def cycle(y, x, N, M):
    if y < 0:
        y = N - 1
    elif N <= y:
        y = 0

    if x < 0:
        x = M - 1
    elif M <= x:
        x = 0
    return y, x


def backtrak(y, x, d, grid, cand, N, M, visit):
    if cand and [y, x, d] in cand:
        for i, v in enumerate(cand):
            if [y, x, d] == v:
                return len(cand) - i

    if visit[d][y][x] == True:
        return 0

    cand.append([y, x, d])
    visit[d][y][x] = True
    ny, nx = y + movdir[d][0], x + movdir[d][1]
    if not (0 <= ny < N and 0 <= nx < M):
        ny, nx = cycle(ny, nx, N, M)

    if grid[ny][nx] == "R":
        d = right(d)
    elif grid[ny][nx] == "L":
        d = left(d)

    return backtrak(ny, nx, d, grid, cand, N, M, visit)


def solution(grid):
    answer = []
    N, M = len(grid), len(grid[0])
    visit = [
        [[False for col in range(M)] for row in range(N)] for _ in range(4)
    ]

    for i in range(N):
        for j in range(M):
            for k in range(4):
                if visit[k][i][j] == False:
                    cand = []
                    temp = backtrak(i, j, k, grid, cand, N, M, visit)
                    if temp != 0:
                        answer.append(temp)

    return sorted(answer)


import sys

input = sys.stdin.readline
_input = list(input().split())
print(solution(_input))
