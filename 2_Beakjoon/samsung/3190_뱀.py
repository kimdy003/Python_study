import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]
dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)

for _ in range(int(input())):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 2  # 사과 위치

q = deque()
for _ in range(int(input())):
    x, c = input().split()
    q.append([int(x), c])

time = 0
snake, d = deque([[0, 0]]), 0
board[0][0] = 1
while True:
    if q and time == q[0][0]:
        _, c = q.popleft()
        if c == "L":
            d = 3 if d - 1 == -1 else d - 1
        else:
            d = 0 if d + 1 == 4 else d + 1
    time += 1

    y, x = snake[-1]
    ny, nx = y + dy[d], x + dx[d]
    if ny < 0 or N <= ny or nx < 0 or N <= nx or board[ny][nx] == 1:
        print(time)
        break

    if board[ny][nx] == 0:  # apple 존재
        ty, tx = snake.popleft()
        board[ty][tx] = 0

    board[ny][nx] = 1
    snake.append([ny, nx])
