import sys
from collections import defaultdict

input = sys.stdin.readline
movdir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

N = int(input())
board = [[0] * N for _ in range(N)]
likedict = defaultdict(list)

for _ in range(N * N):
    _input = list(map(int, input().split()))
    likedict[_input[0]] = _input[1:]

    max_y, max_x = 0, 0
    max_empty, max_like = -1, -1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                like, empty = 0, 0
                for k in range(4):
                    ny, nx = i + movdir[k][0], j + movdir[k][1]
                    if 0 <= ny < N and 0 <= nx < N:
                        if board[ny][nx] in likedict[_input[0]]:
                            like += 1
                        elif board[ny][nx] == 0:
                            empty += 1

                if max_like < like or (max_like == like and max_empty < empty):
                    max_like, max_empty = like, empty
                    max_y, max_x = i, j

    board[max_y][max_x] = _input[0]

ans = 0
for i in range(N):
    for j in range(N):
        like = 0
        for k in range(4):
            ny, nx = i + movdir[k][0], j + movdir[k][1]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] in likedict[board[i][j]]:
                    like += 1

        if like != 0:
            ans += 10 ** (like - 1)

print(ans)
