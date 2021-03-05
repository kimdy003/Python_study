def solution(n, s):
    answer = [0]*n

    div = s//n
    rest = s%n

    if div == 0:
        return [-1]
    
    for i in range(n):
        answer[i] = div
        if(n-rest <= i):
            answer[i] += 1
    
    return answer

print(solution(4, 18))