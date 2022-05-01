'''
2021.11.06
4991_로봇 청소기
'''
import sys
from collections import deque

input = sys.stdin.readline
movdir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

M, N = map(int, input().split())
board = [[0]* M for _ in range(N)]

robot, dirtys = [], []
for i in range(N):
    for j, s in enumerate(input()):
        if s == 'o':
            robot = [i, j]
        elif s == '*':
            dirtys.append([i, j])
        else:
            board[i][j] = -1


def bfs(end):
    visit = [[True] * M for _ in range(N)]
    q = deque([robot])
    visit[robot[0]][robot[1]] = False
    


while True:
    # 끝내기

    # 제일 가까운 dirty 고르기
    for dirty in dirtys:
        bfs(dirty)