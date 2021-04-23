def check(lst):
    stack = []

    for l in lst:
        if l in '[{(':
            stack.append(l)
        else:
            if not stack and l in ')}]':
                return False
            if l == ')' and stack[-1] in '{[':
                return False
            if l == '}' and stack[-1] in '([':
                return False
            if l == ']' and stack[-1] in '({':
                return False
            
            stack.pop()
    
    if stack:
        return False
    return True


def solution(s):
    answer = 0
    lst = [i for i in s]

    idx = 0
    while idx < len(s):
        if check(lst):
            answer += 1

        lst.append(lst[0])
        del lst[0]
        idx += 1

    return answer

print(solution("[](){}"))