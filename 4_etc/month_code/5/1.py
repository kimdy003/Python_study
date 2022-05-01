import math


def check(num):
    if math.sqrt(num) % 1 == 0:
        return False  # 홀수
    return True


def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        if check(i):
            answer += i
        else:
            answer -= i

    return answer