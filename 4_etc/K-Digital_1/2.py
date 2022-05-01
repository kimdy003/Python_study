def check(Str):
    stack = []
    try:
        for i in range(len(Str)):
            if Str[i] == '(':
                stack.append(i)
            else:
                stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False
    except:
        return False

    
def solution(arr1, arr2):
    answer = 0
    
    for i in arr1:
        for j in arr2:
            Str = i+j
            if check(Str):
                answer += 1
            
    return answer