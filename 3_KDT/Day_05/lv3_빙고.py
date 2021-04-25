#
#  lv3_빙고.py
#  빙고
#
#  Create by 김도영 on 2021/04/23
#


def solution(board, nums):
    answer = 0
    n = len(board)
    nums = dict.fromkeys(nums, True)

    row_list, col_list = [0] * n, [0] * n
    row_diagonal, col_diagonal = 0, 0

    for i in range(n):
        for j in range(n):
            if board[i][j] in nums:
                board[i][j] = 0
                row_list[i] += 1
                col_list[i] += 1

                if i == j:
                    row_diagonal += 1
                if n - 1 - i == j:
                    col_diagonal += 1

    answer += sum([1 for l in row_list if l == n])
    answer += sum([1 for l in col_list if l == n])
    answer += 1 if row_diagonal == n else 0
    answer += 1 if col_diagonal == n else 0

    return answer
