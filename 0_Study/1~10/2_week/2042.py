import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [0] + [int(input()) for _ in range(N)]
Sum_lst = [0] * (N + 1)
for i in range(1, N + 1):
    Sum_lst[i] = Sum_lst[i - 1] + lst[i]

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:  # 변경
        temp = c - lst[b]
        lst[b] = c
        for i in range(b, N + 1):
            Sum_lst[i] += temp

    else:  # 출력
        print(Sum_lst[c] - Sum_lst[b - 1])
