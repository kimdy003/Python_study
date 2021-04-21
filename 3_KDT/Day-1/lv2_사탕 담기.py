#
#  lv2_사탕 담기.py
#  lv2_사탕 담기
#
#  Create by 김도영 on 2021/04/20.
#


from itertools import combinations

def solution(m, weights):
    answer = 0
    
    for cnt in range(1, len(weights)):
        totals = map(sum, combinations(weights, cnt))
        for total in totals:
            if total == m:
                answer += 1  
                
    return answer