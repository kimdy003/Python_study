#
#  lv1_예산_소팅.py
#  lv1_예산_소팅
#
#  Create by 김도영 on 2021/04/21
#


def solution(d, budget):
    answer = 0
    d.sort()
    
    sum = 0
    for i in d:
        sum += i
        if budget >= sum:
            answer += 1
            
    return answer