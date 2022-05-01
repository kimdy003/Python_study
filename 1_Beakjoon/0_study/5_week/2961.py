"""
2021.11.13
2961_도영이가 만든 맛있는 음식
"""
import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    ans = float("inf")

    for i in range(1, 1 << N):
        S, B = 1, 0

        for j in range(N):
            if i & (1 << j):
                S *= info[j][0]
                B += info[j][1]

        temp = abs(S - B)
        ans = min(ans, temp)
    print(ans)


solve()
