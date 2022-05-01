import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    dist = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5

    if dist == 0 and r_1 == r_2:
        print(-1)
    elif abs(r_1 - r_2) == dist or r_1 + r_2 == dist:
        print(1)
    elif abs(r_1 - r_2) < dist < (r_1 + r_2):
        print(2)
    else:
        print(0)
