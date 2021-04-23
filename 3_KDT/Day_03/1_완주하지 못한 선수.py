#
#  1_완주하지 못한 선수.py
#  완주하지 못한 선수
#
#  Create by 김도영 on 2021/04/22
#


def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return p[-1]