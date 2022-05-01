import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
cnt = 0

for j in range(len(coin) - 1, -1, -1):
    if K // coin[j] == 0:
        continue
    else:
        cnt += K // coin[j]
        K %= coin[j]

print(cnt)
