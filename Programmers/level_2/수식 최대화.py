def calc(order, n, expression):
    if n == 2:
        return str(eval(expression))
    if order[n] == "*":
        res = eval('*'.join([calc(order, n+1, e) for e in expression.split("*")]))
    if order[n] == "+":
        res = eval('+'.join([calc(order, n+1, e) for e in expression.split("+")]))
    if order[n] == "-":
        res = eval('-'.join([calc(order, n+1, e) for e in expression.split("-")]))
    return str(res)

def solution(expression):
    answer = 0
    orders = [["+","-", " *"],
                ["+","*", "-"],
                ["-", "+", "*"],
                ["-", "*", "+"],
                ["*", "+", "-"],
                ["*", "-", "+"]]
    
    for order in orders:
        res = int(calc(order, 0, expression))
        answer = max(answer, abs(res))
    return answer