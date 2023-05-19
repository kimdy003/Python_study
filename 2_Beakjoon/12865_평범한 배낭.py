import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    item = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            weight, value = item[i]

            if j < weight:
                dp[i][j] = dp[i - 1][j]  # weight보다 작으면 위의 값을 그대로 가져온다.
            else:
                dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

    for i in range(N + 1):
        print(dp[i])

    print(dp[N][K])
