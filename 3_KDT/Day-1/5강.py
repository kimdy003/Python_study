# 
#  5강.py
#  재귀적 이진탐색
#
#  Created by 김도영 on 2021/04/20.
#

def solution(L, x, l, u):
    if u < l:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)
    else:
        return solution(L, x, mid+1, u)

