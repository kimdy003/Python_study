def operation(num1, num2, op):
    if op == "+":
        return num1 + num2
    if op == "-":
        return num1 - num2
    if op == "*":
        return num1 * num2


def calculate(exp, order):
    for ord in order:
        stack = []
        while len(exp) != 0:
            temp = exp.pop(0)
            if temp == ord:
                stack.append(operation(stack.pop(), exp.pop(0), ord))
            else:
                stack.append(temp)
        exp = stack
    return abs(exp[0])


# 숫자와 수식 나누기
def stringSplit(expression):
    array = []
    temp = ""
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            array.append(int(temp))
            array.append(i)
            temp = ""
    array.append(int(temp))
    return array


def solution(expression):
    orders = [("+", "-", "*"), ("+", "*", "-"), ("-", "+", "*"), ("-", "*", "+"), ("*", "+", "-"), ("*", "-", "+")]
    result = []
    expression = stringSplit(expression)
    for order in orders:
        result.append(calculate(expression[:], order))
    return max(result)


print(solution("100-200*300-500+20"))
