# 
#  2강_2.py
#  리스트에서 원소 찾아내기
#
#  Created by 김도영 on 2021/04/20.
#

def solution(L, x):
    answer = [i for i, k in enumerate(L) if k == x]
    
    return answer if len(answer) != 0 else [-1]