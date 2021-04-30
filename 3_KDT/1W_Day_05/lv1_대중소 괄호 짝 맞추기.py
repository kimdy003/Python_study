#
#  lv1_대중소 괄호 짝 맞추기.py
#  대중소 괄호 짝 맞추기
#
#  Create by 김도영 on 2021/04/23
#

dic = {")": "(", "}": "{", "]": "["}


def solution(S):
    stack = []

    for s in S:
        if s in "({[":
            stack.append(s)
        else:
            if not stack or dic[s] != stack[-1]:
                return False

            stack.pop()

    return True if not stack else False