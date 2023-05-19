from functools import cmp_to_key


def cmp(a, b):
    t1, t2 = a + b, b + a
    t1, t2 = int(t1), int(t2)
    return (t1 > t2) - (t1 < t2)  # t1이 크다면 1 , t2가 크다면 -1, 같으면 0


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(cmp), reverse=True)
    return str(int("".join(numbers)))
