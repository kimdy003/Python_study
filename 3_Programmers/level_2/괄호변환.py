# 괄호변환


def divide(p):
    count = [0, 0]
    for i in p:
        if i == "(":
            count[0] += 1
        else:
            count[1] += 1
        if count[0] == count[1]:
            break
    return p[: sum(count)], p[sum(count) :]


def check(p):
    stack = []
    try:
        for i in p:
            if i == "(":
                stack.append("(")
            else:
                stack.pop()
        return True
    except:
        return False


def convert(u):
    temp = ""
    for i in u:
        if i == "(":
            temp += ")"
        else:
            temp += "("
    return temp


def solution(p):
    answer = ""

    while len(p) != 0:
        u, p = divide(p)
        if check(u):
            answer += u
        else:
            answer += "(" + solution(p) + ")" + convert(u[1:-1])
            break
    return answer


print(solution("()))((()"))
