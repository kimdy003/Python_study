#
#  상어 초등학교
#

import sys
from collections import defaultdict


input = sys.stdin.readline
N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
movdir = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # 상하좌우
likedict = defaultdict(list)

for _ in range(N * N):
    _input = list(map(int, input().split()))
    likedict[_input[0]] = _input[1:]

    max_y, max_x = 0, 0
    max_like, max_empty = -1, -1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                likecnt, emptycnt = 0, 0
                for k in range(4):
                    ny, nx = i + movdir[k][0], j + movdir[k][1]
                    if 0 <= ny < N and 0 <= nx < N:
                        if board[ny][nx] in _input[1:]:
                            likecnt += 1
                        elif board[ny][nx] == 0:
                            emptycnt += 1

                if max_like < likecnt or (
                    max_like == likecnt and max_empty < emptycnt
                ):
                    max_y, max_x = i, j
                    max_like, max_empty = likecnt, emptycnt

    board[max_y][max_x] = _input[0]

ans = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        like = likedict[board[i][j]]
        for k in range(4):
            ny, nx = i + movdir[k][0], j + movdir[k][1]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] in like:
                    cnt += 1

        if cnt != 0:
            ans += 10 ** (cnt - 1)
print(ans)
