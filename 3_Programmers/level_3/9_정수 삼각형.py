def solution(triangle):
    dp = [[0]*len(t) for t in triangle]

    dp[0][0] = triangle[0][0]

    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+triangle[i+1][j+1])
    
    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))