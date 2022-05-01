#체육복

def solution(n, lost, reserve):
    set_lost = list(set(lost)-set(reserve))
    set_reserve = list(set(reserve) - set(lost))
    answer = n-len(set_lost)
    
    for i in set_lost:
        for idx, j in enumerate(set_reserve):
            if j == 0: continue
            if i-1 == j:
                answer += 1
                set_reserve[idx] = 0
                break
            elif i+1 == j:
                answer += 1
                set_reserve[idx] = 0
                break
                
    return answer