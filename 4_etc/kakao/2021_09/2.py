def convert(n, q):
    base = ""

    while n > 0:
        n, mod = divmod(n, q)
        base += str(mod)

    return base[::-1]


def prime_list(n):
    sieve = [False, False] + [True] * (n - 1)
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    lst = [i for i in range(2, n + 1) if sieve[i]]
    return lst


def prim(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n // i * i == n:
            return False
        i += 2

    return True


def solution(N, k):
    answer = 0
    prime = prime_list(1000000)
    if k != 10:
        N = convert(N, k)
        print(len(N))

    lst = [int(s) for s in str(N).split("0") if len(s)]
    # lst, temp = [], ''
    # for n in str(N):
    #     if n != '0':
    #         temp += n
    #     else:
    #         if len(temp):
    #             lst.append(int(temp))
    # else:
    #     if len(temp):
    #             lst.append(int(temp))

    for l in lst:
        if l in prime:
            answer += 1
    print(N)
    print(lst)
    return answer


print(solution(1000000, 3))
