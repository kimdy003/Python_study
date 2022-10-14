import sys

input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]


def solve(N, lst):
    dp = [0] * (N + 1)

    for i in range(len(lst) + 1):
        for j, [t, p] in enumerate(lst[:i]):
            dp[i] = max(dp[i], dp[j])

            if j + t == i:
                dp[i] = max(dp[i], dp[j] + p)

    print(dp)
    print(max(dp))
    return


solve(N, lst)
# solve(7, [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]])
