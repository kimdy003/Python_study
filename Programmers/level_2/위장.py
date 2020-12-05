def solution(clothes):
    answer = {}
    
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    cnt = 1
    for i, v in enumerate(answer):
        cnt *= (answer[v]+1)
    return cnt-1