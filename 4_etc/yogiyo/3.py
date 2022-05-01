import random


def solution(A):
    N = len(A)
    ans = N

    while ans > 0:
        for i in range(0, N - ans + 1):
            temp = A[i : i + ans]
            count = set(temp)
            if len(count) <= 2:
                return ans
        ans -= 1


lst = [random.randint(0, 1000000000) for _ in range(100000)]
print(solution(lst))
