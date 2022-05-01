def check(pivot, num, answer):
    while True:
        temp = pivot ^ num

        cnt = 0
        while True:
            if temp == 0 or cnt > 2:
                break
            if (temp & 1) == 1:
                cnt += 1
            temp >>= 1

        if 1 <= cnt <= 2:
            answer.append(num)
            return

        num += 1


def solution(numbers):
    answer = []

    for number in numbers:
        check(number, number + 1, answer)

    return answer


print(solution([2, 7]))