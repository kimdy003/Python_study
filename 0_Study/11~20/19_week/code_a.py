import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    point = [list(map(int, input().split())) for _ in range(3)]
    # 정수, 음수가 아니고, 한 줄에 있지 않는다.
