def solution(student, k):
    answer = 0
    old = [i for i, v in enumerate(student) if v == 1]

    length = len(old)
    idx = -1
    start, end = 0, k - 1
    while end < length:
        left = old[start] - idx
        if end + 1 < length:
            right = old[end + 1] - old[end]
        else:
            right = len(student) - old[end]

        answer += left * right
        idx = old[start]
        start, end = start + 1, end + 1

    return answer


print(solution([0, 1, 0, 0, 1, 1, 0], 2))
