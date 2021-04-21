def solution(A, B):
    answer = 0
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    
    for a in A:
        Min = a
        for b in B:
            if Min < b:
                Min = b
            else:
                break
        if Min == a:
            continue
        else:
            B.remove(Min)
            answer+=1
        
    return answer

print(solution([5,1,3,7],[2,2,6,8]))