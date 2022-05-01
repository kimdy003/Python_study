import sys

input = sys.stdin.readline

ans = [0 for _ in range(10)]
R, C, N = map(int, input().split())
board = [[0] * C for _ in range(R)]

for _ in range(N):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1
