# 21.07.04
# 이동 경로 중 최소값
from collections import deque

INF = 1e9
movdir = [[0,1], [1, 0]]

def bfs(grid, distance, R, C):
    q = deque()
    q.append((0, 0, grid[0][0]))
    distance[0][0] = grid[0][0]

    while q:
        y, x, cost = q.popleft()
        if (y, x) == (R-1, C-1):
            return
        
        for i in range(2):
            ny, nx = y+movdir[i][0], x + movdir[i][1]
            if 0 <= ny < R and 0 <= nx < C:
                if cost + grid[ny][nx] < distance[ny][nx]:
                    distance[ny][nx] = cost + grid[ny][nx]
                    q.append((ny, nx, distance[ny][nx]))


def solution(grid):
    R, C = len(grid), len(grid[0])
    distance = [[1e9] * C for _ in range(R)]
    bfs(grid, distance, R, C)
    print(distance)

    return distance[R-1][C-1]