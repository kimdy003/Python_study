#소수 찾기

import math
from itertools import permutations


def check(n):
    if n < 2:
        return False
    
    k = int(math.sqrt(n))
    for i in range(2, k+1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []

    for cnt in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), cnt)))

        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer))
    return answer

print(solution("110"))