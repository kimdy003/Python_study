def solution(m, n, puddles):
    map = [[0]*(m+1) for _ in range(n+1)]
    map[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            #주의! 문제에서 학교가 있는 위치는 (m, n)이라고 주어짐 즉, (col, row) 순서
            #따라서 puddles도 (col, row) 순서로 되어 있다.
            if [j, i] in puddles:
                map[i][j] = 0
            else:
                map[i][j] = map[i-1][j] + map[i][j-1]

    return map[n][m] % 1000000007

print(solution(4, 3, [[2,3]]))