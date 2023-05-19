def solution(triangle):
    ans = [[0] * len(t) for t in triangle]

    ans[0][0] = triangle[0][0]

    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            ans[i + 1][j] = max(ans[i + 1][j], ans[i][j] + triangle[i + 1][j])
            ans[i + 1][j + 1] = max(ans[i + 1][j + 1], ans[i][j] + triangle[i + 1][j + 1])

    return max(ans[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
