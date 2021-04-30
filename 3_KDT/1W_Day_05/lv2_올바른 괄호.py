#
#  lv2_올바른 괄호.py
#  올바른 괄호
#
#  Create by 김도영 on 2021/04/23
#


def solution(S):
    stack = []

    for s in S:
        if s == "(":
            stack.append(s)
        else:
            if not stack or stack[-1] != "(":
                return False

            stack.pop()
    return False if stack else True