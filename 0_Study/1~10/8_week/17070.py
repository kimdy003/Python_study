import sys
from collections import deque

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
    dp[0][0][1] = 1
    for i in range(N):
        for j in range(1, N):
            

    print(dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1])
