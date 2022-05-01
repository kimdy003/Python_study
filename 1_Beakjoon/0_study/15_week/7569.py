import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = [[] for _ in range(H)]
movdir = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

q = deque([])
for h in range(H):
    for r in range(N):
        tomato[h].append(list(map(int, input().split())))

        for c in range(M):
            if tomato[h][r][c] == 1:
                q.append([h, r, c])

day = -1
while q:
    day += 1

    for _ in range(len(q)):
        h, r, c = q.popleft()

        for dh, dy, dx in movdir:
            next_h, next_r, next_c = h + dh, r + dy, c + dx

            if 0 <= next_h < H and 0 <= next_r < N and 0 <= next_c < M:
                if tomato[next_h][next_r][next_c] == 0:
                    tomato[next_h][next_r][next_c] = 1
                    q.append([next_h, next_r, next_c])

for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[h][r][c] == 0:
                day = -1
                break

print(day)
