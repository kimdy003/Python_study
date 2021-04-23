# 
#  lv1_나머지 한 점.py
#  lv1_나머지 한 점 
#
#  Created by 김도영 on 2021/04/20.
#


def solution(v):
    answer = [0, 0]
    
    for x, y in v:
        answer[0] ^= x
        answer[1] ^= y

    return answer