import sys
from collections import deque

input = sys.stdin.readline

N, M, Q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
movdir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for i in range(N):
    for j in range(M):
        lst[i][j] = [lst[i][j], 0]  # 땅 높이, 비가 내린 날


for day in range(1, Q + 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1

    lst[a][b] = [lst[a][b][0] - c, day]

    result = [a, b, lst[a][b][0], lst[a][b][1]]
    queue = deque([[a, b]])
    visit = [[True for _ in range(M)] for _ in range(N)]
    visit[a][b] = False

    while queue:
        y, x = queue.popleft()
        for dy, dx in movdir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and lst[ny][nx][1] and visit[ny][nx]:
                visit[ny][nx] = False
                queue.append([ny, nx])
                if lst[ny][nx][0] < result[2] or (
                    lst[ny][nx][0] == result[2] and lst[ny][nx][1] < result[3]
                ):
                    result = [ny, nx, lst[ny][nx][0], lst[ny][nx][1]]

    print(result[0] + 1, result[1] + 1)
