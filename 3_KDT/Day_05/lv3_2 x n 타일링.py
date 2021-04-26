#
#  lv3_2 x n 타일링.py
#  2 x n 타일링
#
#  Create by 김도영 on 2021/04/25
#


def solution(n):
    dp = [0, 1, 2] + [0] * (n - 1)

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    return dp[n]