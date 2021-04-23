# 
#  lv1_운송 트럭.py
#  lv1_운송 트럭 
#
#  Created by 김도영 on 2021/04/20.
#

def solution(max_weight, specs, names):
    answer = 1
    dic = {k:int(w) for k, w in specs}
    
    Sum = 0
    for name in names:
        Sum += dic[name]
        if max_weight < Sum:
            answer += 1
            Sum = dic[name]
        
    return answer