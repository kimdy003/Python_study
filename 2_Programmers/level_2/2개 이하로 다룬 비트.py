def check(pivot, answer):
    b = 1
    while True:
        temp = pivot | b
        if temp > pivot:
            answer.append(temp - (b >> 1))
            return

        b <<= 1


def solution(numbers):
    answer = []

    for number in numbers:
        check(number, answer)

    return answer