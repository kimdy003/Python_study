#
#  lv2_짝지어 제거하기.py
#  짝지어 제거하기
#
#  Create by 김도영 on 2021/04/23
#


def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if stack:
        return 0
    return 1
