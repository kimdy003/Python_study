def solution(money):
    if len(money) <= 2:
        return max(money)

    dp1 = [0] * len(money)
    dp2 = dp1[:]

    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])  # 첫 번째 집을 터는 경우
    for i in range(2, len(money) - 1):  # 마지막 집은 털지 못함
        dp1[i] = max(
            dp1[i - 1], money[i] + dp1[i - 2]
        )  # 현재 집을 안 터는 경우, 현재 집을 터는 경우

    dp2[0] = 0
    dp2[1] = money[1]  # 첫 번째 집을 안 터는 경우
    for i in range(2, len(money)):  # 마지막 집까지 털수 있다.
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])

    return max(max(dp1), max(dp2))
