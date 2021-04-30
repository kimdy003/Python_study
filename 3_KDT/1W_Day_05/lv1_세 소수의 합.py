#
#  lv1_세 소수의 합.py
#  세 소수의 합
#
#  Create by 김도영 on 2021/04/23
#

from itertools import combinations


def prime_list(n):
    sieve = [False, False] + [True] * (n - 1)
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i]]


def solution(n):
    ans = 0
    prime = prime_list(n)
    for com in combinations(prime, 3):
        if sum(com) == n:
            ans += 1
    return ans