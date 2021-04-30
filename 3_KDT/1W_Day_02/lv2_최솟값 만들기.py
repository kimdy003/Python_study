#
#  lv2_최솟값 만들기.py
#  lv2_최솟값 만들기
#
#  Create by 김도영 on 2021/04/21
#

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A, B):
        answer += (a*b)

    return answer