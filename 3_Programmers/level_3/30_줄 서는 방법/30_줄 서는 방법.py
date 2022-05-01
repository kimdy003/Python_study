from functools import reduce

def solution(n, k):
    answer = []
    visit = [False]*(n+1)

    idx = n
    while idx != 1:
        for i in range(1, n+1):
            if(visit[i] == True): continue
            num = reduce(lambda x, y: x*y, range(1, idx))
            if k <= num:
                answer.append(i)
                visit[i] = True
                idx -= 1
                break
            k-= num

    for i in range(1, n+1):
        if(visit[i] == True): continue
        answer.append(i)

    return answer

print(solution(3, 5))