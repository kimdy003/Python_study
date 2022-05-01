from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())

ans = 0
start, end = 1, K
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N + 1):
        temp += min(mid // i, N)  # mid보다 작은 수의 합

    if temp >= K:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)