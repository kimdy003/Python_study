def solution(n, money):
    dp = [1] + [0]*n

    for m in money:
        for j in range(m, n+1):
            if(m <= j):
                dp[j] += dp[j-m]
    
    return dp[n] % 1000000007

print(solution(5, [1,2,5]))