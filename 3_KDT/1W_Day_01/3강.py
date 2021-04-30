# 
#  3강.py
#  이진탐색
#
#  Created by 김도영 on 2021/04/20.
#

def solution(L, x):
    lower, upper = 0, len(L)-1
    idx = -1
    
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            idx = middle
            break
            
        elif L[middle] < x:
            lower = middle+1
        else:
            upper = middle-1
    
    return idx