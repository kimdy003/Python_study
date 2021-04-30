#
#  lv1_좌석 구매.py
#  좌석 구매
#
#  Create by 김도영 on 2021/04/23
#


def solution(seat):
    answer = -1
    lst = set(tuple(s) for s in seat)

    return len(lst)