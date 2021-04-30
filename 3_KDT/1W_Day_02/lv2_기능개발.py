#
#  lv2_기능개발.py
#  lv2_기능개발
#
#  Create by 김도영 on 2021/04/21
#

def solution(progresses, speeds):
    answer = []
    lst = []
    for p, s in zip(progresses, speeds):
        p = 100-p
        temp = p // s
        if p%s:
            temp += 1
        lst.append(temp)
        
    pivot, cnt = lst[0], 1
    for i in range(1, len(lst)):
        if pivot < lst[i]:
            answer.append(cnt)
            pivot, cnt = lst[i], 1
        else:
            cnt += 1
    else:
        answer.append(cnt)
        
    return answer