#
#  lv3_N-Queen.py
#  N-Queen
#
#  Create by 김도영 on 2021/04/23
#


def check(queen, n, row, col):
    for r in range(row):  # 그 전의 Queen들과 비교
        q = queen[r]  # col 위치

        if q == col:  # 같은 열인지 검사
            return False

        a = abs(q - col)
        b = row - r
        if a == b:  # 같은 대각선인지 검사
            return False
    return True


def place_queen(queen, n, row):
    if row == n:  # 체스판 끝까지 도착하면
        return 1  # Queen이 알맞게 놓아진것으로 return 1

    cnt = 0
    for col in range(n):  # col의 값이 Queen이 놓일 위치가 된다.
        if check(queen, n, row, col) == True:  # 이전에 놓았던 Queen들과 비교를 한 후
            queen[row] = col  # 괜찮다면 Queen을 그 자리에 위치
            cnt += place_queen(queen, n, row + 1)  # 재귀
    return cnt


def solution(n):
    queen = [0] * n
    answer = place_queen(queen, n, 0)

    return answer