def solution(alp, cop, problems):
    max_alp = max_cop = time = 0
    for a, b, _, _, c in problems:
        max_alp = max(max_alp, a)
        max_cop = max(max_cop, b)
        time += c

    # 목표 알고력
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = int(1e9)
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    nxt_alp, nxt_cop = min(max_alp, i + alp_rwd), min(max_cop, j + cop_rwd)
                    dp[nxt_alp][nxt_cop] = min(dp[nxt_alp][nxt_cop], dp[i][j] + cost)

    return dp[-1][-1]
