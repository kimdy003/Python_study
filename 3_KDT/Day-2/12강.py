#
#  12강.py
#  중위표현 수식 -> 후위표현 수식 
#
#  Create by 김도영 on 2021/04/21
#


class ArrayStack:
    
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''

    for s in S:
        if s == '(':
            opStack.push(s)

        elif s in prec:
            if opStack.isEmpty():
                opStack.push(s)
            else:
                while not opStack.isEmpty():
                    if prec[s] <= prec[opStack.peek()]:
                        answer += opStack.pop()
                    else: break
                opStack.push(s)

        elif s == ')':
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        
        else:
            answer += s
        

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer

print(solution("A*B+C"))