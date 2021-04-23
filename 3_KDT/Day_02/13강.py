#
#  13강.py
#  후위표현 수식 계산 
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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for s in tokenList:
        if s == '(':
            opStack.push(s)

        elif s in prec:
            if opStack.isEmpty():
                opStack.push(s)
            else:
                while not opStack.isEmpty():
                    if prec[s] <= prec[opStack.peek()]:
                        postfixList.append(opStack.pop())
                    else: break
                opStack.push(s)

        elif s == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        
        else:
            postfixList.append(s)
        

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    Stack = ArrayStack()

    for token in tokenList:
        if type(token) is int:
            Stack.push(token)

        else:
            b, a = Stack.pop(), Stack.pop()
            if token == '+':
                Stack.push(a+b)

            elif token == '-':
                Stack.push(a-b)

            elif token == '*':
                Stack.push(a*b)

            elif token == '/':
                Stack.push(a/b)

    
    return Stack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val