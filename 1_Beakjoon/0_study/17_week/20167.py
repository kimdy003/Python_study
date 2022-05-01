import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

ans, total = 0, 0
for num in lst:
    total += num
    if total == K:
        total = num
        continue
    elif total > K:
        ans += total - K
        total = 0

print(ans)