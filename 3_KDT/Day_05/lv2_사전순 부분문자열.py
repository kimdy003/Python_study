#
#  lv2_사전순 부분문자열.py
#  사전순 부분문자열
#
#  Create by 김도영 on 2021/04/24
#


def solution(S):
    stack = []

    for s in S:
        while stack and stack[-1] < s:
            stack.pop()

        stack.append(s)
    return "".join(stack)


print(solution("xyb"))