def solution(n, stations, w):
    answer = 0
    
    idx = 1
    step = w*2+1
    for stat in stations:
        left = stat - w

        if idx < left:
            count = left - idx
            answer += count // step
            if count%step != 0:
                answer += 1
                
        idx = stat+w+1
    
    if idx <= n:
        count = n - idx+1
        answer += count // step
        if count %step != 0:
            answer += 1

    return answer
    
print(solution(16, [9], 2))