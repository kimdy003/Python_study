def check(mid, stones, k):
    cnt = 0
    for stone in stones:
        if stone <= mid:
            cnt += 1
        else:
            cnt = 0
        if k <= cnt:
            return True
    return False

def solution(stones, k):
    Min, Max = 1, max(stones)+1
    
    while(Min < Max-1):
        mid = (Min+Max)//2
        
        if check(mid, stones, k):
            Max = mid
        else:
            Min = mid
    
    return Max