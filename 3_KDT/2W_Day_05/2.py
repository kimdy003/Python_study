def solution(arr):
    answer = 1
    arr.sort(key=lambda x : (x[1], x[0]))
    
    prev = arr[0][1]
    for nxt in arr[1:]:
        if prev <= nxt[0]:
            prev = nxt[1]
            answer += 1
    
    return answer


print(solution([[1, 2], [2, 4], [2, 2]]))