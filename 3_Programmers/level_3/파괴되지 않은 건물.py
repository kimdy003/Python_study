def solution(board, skills):
    answer = 0
    N, M = len(board), len(board[0])
    sumBoard = [[0] * (M + 1) for _ in range(N + 1)]

    for skill in skills:
        if skill[0] == 1:
            sumBoard[skill[1]][skill[2]] -= skill[5]
            sumBoard[skill[1]][skill[4] + 1] += skill[5]
            sumBoard[skill[3] + 1][skill[2]] += skill[5]
            sumBoard[skill[3] + 1][skill[4] + 1] -= skill[5]
        else:
            sumBoard[skill[1]][skill[2]] += skill[5]
            sumBoard[skill[1]][skill[4] + 1] -= skill[5]
            sumBoard[skill[3] + 1][skill[2]] -= skill[5]
            sumBoard[skill[3] + 1][skill[4] + 1] += skill[5]

    for j in range(M + 1):
        for i in range(N):
            sumBoard[i + 1][j] += sumBoard[i][j]

    for i in range(N + 1):
        for j in range(M):
            sumBoard[i][j + 1] += sumBoard[i][j]

    for i in range(N):
        for j in range(M):
            if board[i][j] + sumBoard[i][j] > 0:
                answer += 1

    return answer


print(
    solution(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
    )
)
