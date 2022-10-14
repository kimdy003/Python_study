"""
2021.10.22
21610_마법사 상어와 비바라기
"""
import sys
from collections import deque

input = sys.stdin.readline


def Print(arr):
    print()
    for i in range(len(arr)):
        print(arr[i])


def Move_Rain(cloud, d, s, board):
    # 구름 이동 & 비 내리기
    visit = [[True] * N for _ in range(N)]
    length = len(cloud)
    for _ in range(length):
        y, x = cloud.popleft()
        # N을 더해 음의 수가 나오는 것을 해결
        y, x = (N + y + movdir[d][0] * s) % N, (N + x + movdir[d][1] * s) % N
        board[y][x] += 1
        visit[y][x] = False
        cloud.append([y, x])

    # 물복사버그 마법 실행
    for y, x in cloud:
        cnt = 0
        # 대각선 좌표 뽑기
        for k in range(1, 8, 2):
            ny, nx = y + movdir[k][0], x + movdir[k][1]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] > 0:
                    cnt += 1

        board[y][x] += cnt
    return visit


def Created_Cloud(board, visit):
    # 2이상 모든 칸 & 물의 양 2 줄어든다.
    # cloud에 있는 칸이 아니어야한다.
    temp = deque([])
    for i in range(N):
        for j in range(N):
            # 이 부분에서 시간 초과가 남
            # if board[i][j] >= 2 and [i, j] not in cloud:

            if board[i][j] >= 2 and visit[i][j]:
                board[i][j] -= 2
                temp.append([i, j])
    return temp


movdir = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cloud = deque([[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]])

# 좌표, 방향 -1 해줘야함
for _ in range(M):
    d, s = map(int, input().split())
    d -= 1

    # 구름 이동 & 비 내리기 & 물복사버그마법
    visit = Move_Rain(cloud, d, s, board)

    # 구름 생성
    cloud = Created_Cloud(board, visit)

print(sum([sum(board[i]) for i in range(N)]))
