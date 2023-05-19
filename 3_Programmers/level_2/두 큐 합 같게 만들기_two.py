def solution(queue1, queue2):
    target = (sum(queue1) + sum(queue2)) // 2
    cur = sum(queue1)
    queue3 = queue1 + queue2 + queue1

    left = 0
    right = len(queue1) - 1
    answer = 0
    while True:
        if cur == target:
            return answer
        if cur < target:
            right += 1
            if right >= len(queue3):
                return -1
            cur += queue3[right]
        else:
            cur -= queue3[left]
            left += 1
        answer += 1
