import sys

input = sys.stdin.readline

N = int(input())
dp = [0, 0, 3] + [0, 2] * N

for i in range(4, N + 1, 2):
    dp[i] += 3 * dp[i - 2]
    dp[i] += sum([dp[j] * 2 for j in range(i - 4, -1, -2)])

print(dp[N])
