#
#  lv2_주사위 게임.py
#  주사위 게임
#
#  Create by 김도영 on 2021/04/25
#


from itertools import product


def solution(monster, S1, S2, S3):
    p = product(range(S1), range(S2), range(S3))
    case = len([x for x in p if sum(x) + 4 not in monster])
    return int(case / (S1 * S2 * S3) * 1000)