def solution(citations):
    answer = 0

    for i in range(1, 10001):
        temp_1 = [x for x in citations if x >= i]
        temp_2 = [x for x in citations if x < i]
        if len(temp_1) >= i and len(temp_2) <= i:
            answer = i

    return answer


print(solution([3, 0, 6, 1, 5]))
