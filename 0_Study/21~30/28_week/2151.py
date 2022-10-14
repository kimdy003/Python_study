import sys
from copy import deepcopy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N = int(input())
board, mirror = [], []
door = []
movdir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for i in range(N):
    board.append(list(input().strip()))
    for j in range(N):
        if board[i][j] == "!":
            mirror.append((i, j))
            board[i][j] = "."

        if board[i][j] == "#":
            door.append((i, j))


def BFS():
    q = deque()
    q.append(door[0])
    visit = [[True] * N for _ in range(N)]
    visit[door[0][0]][door[0][1]] = False

    while q:
        y, x = q.popleft()

        for dy, dx in movdir:
            ny, nx = y + dy, x + dx

            if visit[ny][nx] == True:
                visit[ny][nx] = False

                if board[ny][nx] == ".":
                    while True:
                        nny, nnx = ny + dy, nx + dx


for i in range(1, len(board)):
    for com in combinations(mirror, i):
        for y, x in com:
            board[y][x] = "!"

        if BFS():
            flag = True
            break

        for y, x in com:
            board[y][x] = "."
