import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
board = []
teacher = []
obstacle = []
mov = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for i in range(N):
    board.append(list(input().split()))
    for j in range(N):
        if board[i][j] == "T":
            teacher.append((i, j))
        elif board[i][j] == "X":
            obstacle.append((i, j))


def BFS():
    queue = deque(teacher)
    temp = deepcopy(board)

    while queue:
        y, x = queue.popleft()

        for dy, dx in mov:
            ty, tx = y, x
            while True:
                ny, nx = ty + dy, tx + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if temp[ny][nx] == "X":
                        temp[ny][nx] = "T"
                    elif temp[ny][nx] == "S":
                        return False
                    elif temp[ny][nx] == "O":
                        break
                    ty, tx = ny, nx
                else:
                    break
    return True


flag = False
for data in list(combinations(obstacle, 3)):
    for y, x in data:
        board[y][x] = "O"

    if BFS():
        flag = True
        break
    for y, x in data:
        board[y][x] = "X"

if flag:
    print("YES")
else:
    print("NO")
