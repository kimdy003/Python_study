def solution(board, skills):
    # skill = [type, r1, c1, r2, c2, degree]
    # type 1 - 공격, 2 - 회복
    answer = 0

    for skill in skills:
        for i in range(skill[1], skill[3] + 1):
            for j in range(skill[2], skill[4] + 1):
                if skill[0] == 1:  # 공격
                    board[i][j] -= skill[5]
                else:
                    board[i][j] += skill[5]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                answer += 1

    return answer
