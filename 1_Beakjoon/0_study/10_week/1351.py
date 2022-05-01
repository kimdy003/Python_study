import sys

input = sys.stdin.readline


def calc(idx):
    if idx in dp:
        return dp[idx]
    else:
        dp[idx] = calc(idx // P) + calc(idx // Q)
        return dp[idx]


if __name__ == "__main__":
    N, P, Q = map(int, input().split())
    dp = {0: 1}

    print(calc(N))
