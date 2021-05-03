#
# 3.py
# 단어 퍼즐
#
# Create by 김도영 2021/05/03
#


def solution(strs, t):
    N = len(t)
    dp = [float("inf")] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        j = i - 5 if i > 5 else 0  # 모든 단어 퍼즐은 1이상 5이하

        while j < i:
            if dp[j] + 1 < dp[i] and t[j:i] in strs:
                dp[i] = dp[j] + 1
            j += 1

    return dp[len(t)] if dp[len(t)] != float("inf") else -1


print(solution(["ba", "na", "n", "a"], "banana"))
