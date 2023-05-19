# BFS
from collections import deque

#     상 좌 하 우
dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)
N = input()


def out_ot_range(y, x):  # 격자에서 벗어났는지 확인하는 함수
    return y < 0 or N <= y or x < 0 or N <= x


def bfs(y, x):
    q = deque()

    # 시작 좌표(y, x) 삽입 및 visited 표시
    q.append((y, x))
    visited = [[False] * N for _ in range(N)]  # NxN 격자의 경우
    visited[y][x] = True

    while q:
        sy, sx = q.popleft()
        for d in range(4):
            ny, nx = sy + dy[d], sx + dx[d]

            if out_ot_range(ny, nx) or visited[ny][nx]:
                # 격자에서 벗어났거나, 방문한 좌표의 경우 continue
                continue
            else:
                # do_something()
                q.append((ny, nx))
                visited[ny][nx] = True
