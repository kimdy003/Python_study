# 
#  2강_1.py
#  정렬된 리스트에 원소 삽입
#
#  Created by 김도영 on 2021/04/20.
#

def solution(L, x):
    idx = 0
    for l in L:
        if l < x:
            idx += 1
        else:
            break
            
    L.insert(idx, x)
    return L