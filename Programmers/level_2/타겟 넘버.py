answer = 0

def DFS(numbers, target, idx, val):
    global answer
    n = len(numbers)
    if idx == n:
        if target == val:
            answer += 1
        return
    
    DFS(numbers, target, idx+1, val+numbers[idx])
    DFS(numbers, target, idx+1, val-numbers[idx])
    


def solution(numbers, target):
    global answer
    DFS(numbers, target, 0, 0)
    return answer